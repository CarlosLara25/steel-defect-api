from fastapi import FastAPI, Depends, Request
from contextlib import asynccontextmanager

from app.inference.schemas import PredictionRequest, ResponseSchema

from app.inference.loader import load_inference_artifacts

from app.inference.service import prediction_service

from app.dependencies import verify_api_key


from uuid import uuid4
from datetime import datetime, timezone

from app.errors.exceptions import PredictionError
from app.errors.handlers import prediction_error_handler

from app.logging_config import configure_logging
import logging

import pandas as pd

configure_logging()

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    (
        app.state.model,
        app.state.preprocessor, 
        app.state.encoder, 
        app.state.metadata,
    ) = load_inference_artifacts()

    yield

app = FastAPI(
    title="Steel Defect Classification API",
    version="0.4.0",
    lifespan=lifespan
)

app.add_exception_handler(
    PredictionError,
    prediction_error_handler,
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.middleware("http")
async def add_request_id(request: Request, call_next):

    request_id = str(uuid4())

    request.state.request_id = request_id

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id

    return response


@app.post("/predict", response_model=ResponseSchema)
def prediction(request: Request,
               data_request: PredictionRequest,
               _: None = Depends(verify_api_key),
               ):

    request_id = request.state.request_id

    model = app.state.model
    preprocessor = app.state.preprocessor
    encoder = app.state.encoder
    metadata = app.state.metadata

    # Request → DataFrame
    data = data_request.model_dump()
    X = pd.DataFrame([data])

    prediction, confidence = prediction_service(
                                        X,
                                        preprocessor,
                                        model,
                                        encoder
                                        )

    logger.info("Prediction completed")

    response = {
        "request_id":request_id,
        "prediction":prediction,
        "confidence":confidence,
        "model_version":metadata["version"],
        "timestamp":datetime.now(timezone.utc),
        }
    
    return response
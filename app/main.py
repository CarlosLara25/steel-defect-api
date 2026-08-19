from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.inference.schemas import PredictionRequest, ResponseSchema

from app.inference.loader import load_inference_artifacts

from uuid import uuid4
from datetime import datetime, timezone

import pandas as pd

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


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=ResponseSchema)
def prediction(data_request: PredictionRequest):
    model = app.state.model
    preprocessor = app.state.preprocessor
    encoder = app.state.encoder
    metadata = app.state.metadata

    # Request → DataFrame
    data = data_request.model_dump()
    X = pd.DataFrame([data])

    X_transformed = preprocessor.transform(X)

    y_pred = model.predict(X_transformed)
    probabilities = model.predict_proba(X_transformed)

    prediction = encoder.inverse_transform(y_pred)[0]

    confidence = float(probabilities[0][y_pred[0]])

    response = {
        "request_id":str(uuid4()),
        "prediction":prediction,
        "confidence":confidence,
        "model_version":metadata["version"],
        "timestamp":datetime.now(timezone.utc),
        }
    
    return response
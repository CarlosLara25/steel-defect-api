from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.inference.loader import load_inference_artifacts

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
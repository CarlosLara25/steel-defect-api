from fastapi.testclient import TestClient
from app.inference.loader import load_inference_artifacts

from app.main import app

import pytest


client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_unknown_route():
    response = client.get("/heal")

    assert response.status_code == 404


def test_inference_artifacts_loaded():
    with TestClient(app) as client:
        assert client.app.state.model is not None
        assert client.app.state.preprocessor is not None
        assert client.app.state.encoder is not None
        assert client.app.state.metadata is not None

def test_loader_fails_when_artifact_is_missing(monkeypatch):
    monkeypatch.setattr(
        "app.inference.loader.MODEL_PATH",
        "models/selected/nonexistent_model.joblib"
    )

    with pytest.raises(FileNotFoundError):
        load_inference_artifacts()
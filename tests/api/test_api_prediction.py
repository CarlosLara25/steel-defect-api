from fastapi.testclient import TestClient

from app.main import app
from app.inference.schemas import ResponseSchema


def test_predict_valid_request(
    unique_sample_data,
    monkeypatch,
):
    monkeypatch.setattr(
        "app.dependencies.API_KEY",
        "test-key",
    )

    headers = {"X-API-Key": "test-key"}

    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json=unique_sample_data,
            headers=headers,
        )

        assert response.status_code == 200

        result = ResponseSchema.model_validate(response.json())

        assert result.prediction in client.app.state.encoder.classes_

def test_predict_missing_required_feature(unique_sample_data,
    monkeypatch,
):
    monkeypatch.setattr(
        "app.dependencies.API_KEY",
        "test-key",
    )

    headers = {"X-API-Key": "test-key"}

    incomplete_sample = unique_sample_data.copy()
    incomplete_sample.pop("X_Minimum")

    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json=incomplete_sample,
            headers=headers,
        )
 
        assert response.status_code == 422


def test_predict_invalid_feature_value(
    unique_sample_data,
    monkeypatch,
    ):

    monkeypatch.setattr(
        "app.dependencies.API_KEY",
        "test-key",
    )

    headers = {"X-API-Key": "test-key"}

    invalid_sample = unique_sample_data.copy()

    NEGATIVE_VALUE = -1
    invalid_sample["X_Minimum"] = NEGATIVE_VALUE

    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json=invalid_sample,
            headers=headers
        )

        assert response.status_code == 422



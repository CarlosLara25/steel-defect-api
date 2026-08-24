from fastapi.testclient import TestClient

from app.main import app



def test_predict_with_valid_api_key(
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

def test_predict_with_invalid_api_key(
    unique_sample_data,
    monkeypatch,
):
    monkeypatch.setattr(
        "app.dependencies.API_KEY",
        "test-key",
    )

    headers = {"X-API-Key": "wrong-key"}

    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json=unique_sample_data,
            headers=headers,
        )

    assert response.status_code == 401

def test_predict_without_api_key(
    unique_sample_data
    ):
    
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json=unique_sample_data,
        )

    assert response.status_code == 401

    
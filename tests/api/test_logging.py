import logging

from fastapi.testclient import TestClient

from app.main import app

def test_successful_prediction_is_logged(
                      unique_sample_data,
                            monkeypatch,
                            caplog,
                            ):

    monkeypatch.setattr(
        "app.dependencies.API_KEY",
        "test-key",
    )

    headers = {"X-API-Key": "test-key"}

    with TestClient(app) as client:

        with caplog.at_level(logging.INFO):
            response = client.post(
                "/predict",
                json=unique_sample_data,
                headers={"X-API-Key": "test-key"},
            )

    assert response.status_code == 200

    assert any(
        "Prediction completed" in record.message
        for record in caplog.records
    )
from fastapi.testclient import TestClient

from app.main import app

import logging


def test_prediction_error_returns_500(
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

        def fail_prediction(*args, **kwargs):
            raise ValueError("Forced prediction failure")

        monkeypatch.setattr(
            client.app.state.model,
            "predict",
            fail_prediction,
        )

        with caplog.at_level(logging.ERROR):
            response = client.post(
                "/predict",
                json=unique_sample_data,
                headers=headers,
            )

    body = response.json()

    assert response.status_code == 500
    assert body["error"] == "prediction_failed"
    assert body["detail"] == "An internal prediction error occurred."

    request_id = body["request_id"]

    assert any(
        "Prediction failed" in record.message
        and request_id in record.message
        for record in caplog.records
    )



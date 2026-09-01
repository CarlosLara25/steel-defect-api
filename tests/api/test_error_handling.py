from fastapi.testclient import TestClient

from app.main import app



def test_prediction_error_returns_500(
                            unique_sample_data,
                            monkeypatch,
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

        response = client.post(
            "/predict",
            json=unique_sample_data,
            headers=headers,
        )

    body = response.json()

    assert response.status_code == 500
    assert body["error"] == "prediction_failed"
    assert body["detail"] == "An internal prediction error ocurred."
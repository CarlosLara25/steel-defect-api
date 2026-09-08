from app.errors.exceptions import PredictionError
import logging

#logger = logging.getLogger(__name__)

def prediction_service(X, preprocessor, model, encoder):

        
    try:

        X_transformed = preprocessor.transform(X)

        y_pred = model.predict(X_transformed)
        probabilities = model.predict_proba(X_transformed)

        prediction = encoder.inverse_transform(y_pred)[0]

        confidence = float(probabilities[0][y_pred[0]])

       
        return prediction, confidence

    except Exception as exc:
        raise PredictionError("Prediction failed") from exc



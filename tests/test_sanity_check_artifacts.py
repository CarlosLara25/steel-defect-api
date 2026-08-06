from training.config import (
    PREPROCESSOR_OUTPUT_PATH_SELECTED,
    LABEL_ENCODER_OUTPUT_PATH_SELECTED,
    MODEL_OUTPUT_PATH_SELECTED,
    XGB_SELECTED_LEARNING_RATE,
    XGB_SELECTED_N_ESTIMATORS,
    XGB_SELECTED_MAX_DEPTH,
    XGB_SELECTED_SUBSAMPLE,
    XGB_SELECTED_COLSAMPLE,
)

import pandas as pd
import joblib
import pytest


@pytest.fixture
def sample_data():
    return  pd.DataFrame(
    {
        "X_Minimum": [10, 20, 30],
        "X_Maximum": [40, 50, 60],
        "Y_Minimum": [1000, 1200, 1300],
        "Y_Maximum": [1010, 1220, 1330],
        "Pixels_Areas": [250, 260, 270],
        "X_Perimeter": [10, 12, 14],
        "Y_Perimeter": [30, 40, 50],
        "Sum_of_Luminosity": [20000, 23000, 27000],
        "Minimum_of_Luminosity": [80, 90, 110],
        "Maximum_of_Luminosity": [110, 120, 130],
        "Length_of_Conveyer": [1000, 1500, 2000],
        "TypeOfSteel_A300": [0, 0, 1],
        "TypeOfSteel_A400": [1, 1, 0],
        "Steel_Plate_Thickness": [90, 120, 130],
        "Edges_Index": [0.10, 0.20, 0.30],
        "Empty_Index": [0.35, 0.40, 0.50],
        "Square_Index": [0.10, 0.20, 0.150],
        "Outside_X_Index": [0.010, 0.020, 0.030],
        "Edges_X_Index": [0.50, 0.60, 0.70],
        "Edges_Y_Index": [1.0, 0.95, 0.90],
        "Outside_Global_Index": [0, 0.5, 1],
        "LogOfAreas": [2.3, 2.0, 3.0],
        "Log_X_Index": [1.0, 1.20, 1.30],
        "Log_Y_Index": [1.35, 1.70, 1.90],
        "Orientation_Index": [0.60, 0.70, 0.80],
        "Luminosity_Index": [-0.270, -0.120, 0.030],
        "SigmoidOfAreas": [0.40, 0.70, 0.95]
    })

#---------------------------------
# Test: Loading
#---------------------------------

def test_selected_model_artifact_exists():
    model = joblib.load(MODEL_OUTPUT_PATH_SELECTED)

    assert model is not None


def test_selected_preprocessor_can_be_loaded():
    preprocessor = joblib.load(PREPROCESSOR_OUTPUT_PATH_SELECTED)

    assert preprocessor is not None


def test_selected_encoder_can_be_loaded():
    encoder = joblib.load(LABEL_ENCODER_OUTPUT_PATH_SELECTED)

    assert encoder is not None

#---------------------------------
# Inference sanity check
#---------------------------------

def test_selected_model_can_predict(sample_data):

    model = joblib.load(MODEL_OUTPUT_PATH_SELECTED)
    preprocessor = joblib.load(PREPROCESSOR_OUTPUT_PATH_SELECTED)
    encoder = joblib.load(LABEL_ENCODER_OUTPUT_PATH_SELECTED)

    X_transformed = preprocessor.transform(sample_data)

    prediction_encoded = model.predict(X_transformed)

    prediction = encoder.inverse_transform(prediction_encoded)

    assert len(prediction) == len(sample_data)
    assert all(pred in encoder.classes_ for pred in prediction)


#---------------------------------
# Test: persisted model parameters
#---------------------------------

def test_selected_model_configuration():

    model = joblib.load(MODEL_OUTPUT_PATH_SELECTED)

    assert model.n_estimators == XGB_SELECTED_N_ESTIMATORS
    assert model.learning_rate == XGB_SELECTED_LEARNING_RATE
    assert model.max_depth == XGB_SELECTED_MAX_DEPTH
    assert model.subsample == XGB_SELECTED_SUBSAMPLE
    assert model.colsample_bytree == XGB_SELECTED_COLSAMPLE
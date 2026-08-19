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
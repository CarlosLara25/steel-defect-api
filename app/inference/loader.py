import joblib
import json

from app.config import(
    PREPROCESSOR_OUTPUT_PATH_SELECTED as PREPROCESSOR_PATH,
    MODEL_OUTPUT_PATH_SELECTED as MODEL_PATH,
    LABEL_ENCODER_OUTPUT_PATH_SELECTED as ENCODER_PATH,
    METADATA_PATH_SELECTED as METADATA_PATH,
)


def load_inference_artifacts():
    model = joblib.load(MODEL_PATH)
    preprocessor  = joblib.load(PREPROCESSOR_PATH)
    encoder = joblib.load(ENCODER_PATH)

    with open(METADATA_PATH) as fin:
        metadata = json.load(fin)

    return model, preprocessor, encoder, metadata


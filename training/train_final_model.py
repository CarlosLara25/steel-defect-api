from sklearn.model_selection import train_test_split

from training.baseline_model import build_selected_xgboost
from training.config import (
    RANDOM_SEED,
    TEST_SIZE,
    PREPROCESSOR_OUTPUT_PATH_SELECTED,
    LABEL_ENCODER_OUTPUT_PATH_SELECTED,
    METADATA_PATH_SELECTED,
    MODEL_OUTPUT_PATH_SELECTED,
    MODEL_TYPE,
    VERSION_MODEL,
    XGB_SELECTED_LEARNING_RATE,
    XGB_SELECTED_N_ESTIMATORS,
    XGB_SELECTED_MAX_DEPTH,
    XGB_SELECTED_SUBSAMPLE,
    XGB_SELECTED_COLSAMPLE,
    XGB_SELECTION_METRIC,
    XGB_CV_MACRO_F1,
    XGB_TEST_MACRO_F1,

)
from training.data_loader import load_training_data
from training.target_encoder import fit_label_encoder

from app.preprocessing.pipeline import build_preprocessor

import mlflow
import joblib
import json



def train_selected_xgboost() -> None:
    '''
    Train the selected XGBoost configuration and persist the
    model, preprocessing pipeline, label encoder, and metadata.
    """
    '''

    mlflow.set_experiment(
        "Steel Defect Selected Models"
    )

    with mlflow.start_run(run_name=f"{MODEL_TYPE}_{VERSION_MODEL}"):

        mlflow.set_tag("model_type", MODEL_TYPE)
        mlflow.set_tag("model_version", VERSION_MODEL)
        mlflow.set_tag("training_stage", "selected_model")

        #---------------------------------   
        # Load and split data
        #---------------------------------
    
        X, y = load_training_data()
        X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=TEST_SIZE,
                stratify=y,
                random_state=RANDOM_SEED,
                )
    
        #---------------------------------   
        # Preprocessing
        #---------------------------------
    
        preprocessor = build_preprocessor()
        X_train_transformed = preprocessor.fit_transform(X_train)
    
        joblib.dump(
            preprocessor,
            PREPROCESSOR_OUTPUT_PATH_SELECTED,
            )
           
        # Encoder
        encoder, y_train_encoded = fit_label_encoder(y_train)

        joblib.dump(
            encoder,
            LABEL_ENCODER_OUTPUT_PATH_SELECTED,
        )

        #---------------------------------   
        # Build model
        #---------------------------------   

        model = build_selected_xgboost()

        #----------------------------------------------
        # Metadata
        #----------------------------------------------

        metadata = { "test_size":TEST_SIZE,
                "random_seed": RANDOM_SEED,
                "model_type": MODEL_TYPE,
                "version":VERSION_MODEL,
                "selection_metric": XGB_SELECTION_METRIC,
                "source_experiment":"XGBoost Refinement Experiment 2",
                "cv_macro_f1": XGB_CV_MACRO_F1,
                "test_macro_f1": XGB_TEST_MACRO_F1,
                "max_depth":XGB_SELECTED_MAX_DEPTH,
                "learning_rate":XGB_SELECTED_LEARNING_RATE,
                "n_estimators":XGB_SELECTED_N_ESTIMATORS,
                "subsample":XGB_SELECTED_SUBSAMPLE,
                "colsample_bytree":XGB_SELECTED_COLSAMPLE,
            }


        with open(METADATA_PATH_SELECTED,'w') as fout:
            json.dump(metadata, fout, indent=4)

        #----------------------------------------------
        # Train the model
        #----------------------------------------------

        model.fit(
            X_train_transformed,
            y_train_encoded)


        joblib.dump(
            model,
            MODEL_OUTPUT_PATH_SELECTED,
        )


        #---------------------------------   
        # Log parameters and artifacts
        #---------------------------------   
       
        mlflow.log_params({
            "max_depth":XGB_SELECTED_MAX_DEPTH,
            "learning_rate":XGB_SELECTED_LEARNING_RATE,
            "n_estimators":XGB_SELECTED_N_ESTIMATORS,
            "subsample":XGB_SELECTED_SUBSAMPLE,
            "colsample_bytree":XGB_SELECTED_COLSAMPLE,
        })   

        mlflow.log_artifact(MODEL_OUTPUT_PATH_SELECTED)
        mlflow.log_artifact(PREPROCESSOR_OUTPUT_PATH_SELECTED)
        mlflow.log_artifact(LABEL_ENCODER_OUTPUT_PATH_SELECTED)
        mlflow.log_artifact(METADATA_PATH_SELECTED)


if __name__== "__main__":
    train_selected_xgboost()
    


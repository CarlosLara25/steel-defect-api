from training.baseline_model import build_model
from training.data_loader import load_training_data
from training.config import (
    TEST_SIZE,
    MAX_ITERATIONS,
    RANDOM_SEED,
    MODEL_NAME,
    N_ESTIMATORS,
    CRITERION,
    LOGISTIC_REGRESSION,
    RANDOM_FOREST,
    XGBOOST,
    XGB_MAX_DEPTH,
    XGB_LEARNING_RATE,
    MODEL_OUTPUT_PATH,
    PREPROCESSOR_OUTPUT_PATH,
    CONFUSION_MATRIX_PATH,
    CLASSIFICATION_REPORT_PATH,
    LABEL_ENCODER_OUTPUT_PATH,
)
from training.evaluate import evaluate_model
from training.target_encoder import fit_label_encoder

from app.preprocessing.pipeline import build_preprocessor
from sklearn.model_selection  import train_test_split

import joblib
import mlflow


def train_selected_model() -> dict:
    '''
    Train the baseline classification model.

    The pipeline performs the following steps:

    - Load the dataset.
    - Split the data into training and testing sets.
    - Fit the preprocessing pipeline.
    - Train the baseline model.
    - Evaluate the trained model.
    - Save the fitted preprocessor and model.
    - Return the evaluation metrics.

    '''

    mlflow.set_experiment(
        "Steel Defect Baseline"
    )

    with mlflow.start_run():

        # load data
        X, y = load_training_data()

        # Data separation
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=TEST_SIZE,
            stratify=y,
            random_state=RANDOM_SEED,
            )
        

        if MODEL_NAME == XGBOOST:
            encoder, y_train = fit_label_encoder(y_train)
            joblib.dump(
                encoder,
                LABEL_ENCODER_OUTPUT_PATH,
            )
            y_test = encoder.transform(y_test)


        # build preprocessor
        preprocessor = build_preprocessor()

        # fit and transform training features
        X_train_transformed = preprocessor.fit_transform(X_train)

        # build model
        model = build_model()

        # log parameters
        mlflow.log_param("test_size", TEST_SIZE)
        mlflow.log_param("random_seed", RANDOM_SEED)
        mlflow.log_param("model", MODEL_NAME)

        if MODEL_NAME==LOGISTIC_REGRESSION:
            mlflow.log_param("max_iter", MAX_ITERATIONS)
        elif MODEL_NAME==RANDOM_FOREST:
            mlflow.log_param("N_estimators", N_ESTIMATORS)
            mlflow.log_param("criterion", CRITERION)
        elif MODEL_NAME==XGBOOST:
            mlflow.log_param("max_depth", XGB_MAX_DEPTH)
            mlflow.log_param("learning_rate", XGB_LEARNING_RATE)
        

        # train the model
        model.fit(X_train_transformed, y_train)

        # transform the X_test
        X_test_transformed = preprocessor.transform(X_test)


        y_pred = model.predict(X_test_transformed)

        # Calculate metrics
        evaluation = evaluate_model(y_test=y_test, y_pred=y_pred)

        mlflow.log_metrics(evaluation)


        #  Save preprocessor and model
        #----------------------------------------------
        joblib.dump(
                preprocessor,
                PREPROCESSOR_OUTPUT_PATH,
            )

        joblib.dump(
            model,
            MODEL_OUTPUT_PATH,
        )
        #----------------------------------------------

        # Log artifacts
        mlflow.log_artifact(MODEL_OUTPUT_PATH)
        mlflow.log_artifact(PREPROCESSOR_OUTPUT_PATH)
        mlflow.log_artifact(CONFUSION_MATRIX_PATH)
        mlflow.log_artifact(CLASSIFICATION_REPORT_PATH)

        return evaluation





if __name__== "__main__":
    metrics = train_selected_model()
    print(metrics)

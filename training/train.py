from training.baseline_model import build_baseline_model
from training.data_loader import load_training_data
from training.config import (
    TEST_SIZE,
    MAX_ITERATIONS,
    RANDOM_SEED,
    MODEL_OUTPUT_PATH,
    PREPROCESSOR_OUTPUT_PATH,
    CONFUSION_MATRIX_PATH,
    CLASSIFICATION_REPORT_PATH,
)
from training.evaluate import evaluate_model

from app.preprocessing.pipeline import build_preprocessor
from sklearn.model_selection  import train_test_split

import joblib
import mlflow


def train_baseline_model() -> dict:
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

        # build preprocessor
        preprocessor = build_preprocessor()

        # fit and transform training features
        X_train_transformed = preprocessor.fit_transform(X_train)

        # build model
        model = build_baseline_model()

        # log parameters
        mlflow.log_param("model", "LogisticRegression")
        mlflow.log_param("max_iter", MAX_ITERATIONS)
        mlflow.log_param("test_size", TEST_SIZE)
        mlflow.log_param("random_seed", RANDOM_SEED)


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
    metrics = train_baseline_model()
    print(metrics)

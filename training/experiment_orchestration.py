from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from training.tuning import tune_model
from training.config import (
    RANDOM_SEED,
    TEST_SIZE,
    PREPROCESSOR_OUTPUT_PATH,
    LABEL_ENCODER_OUTPUT_PATH,
    RANDOM_FOREST,
    XGBOOST,
)
from training.data_loader import load_training_data
from training.target_encoder import fit_label_encoder
from training.evaluate import evaluate_model
from training.parameters_distributions import (
    PARAM_DISTRIBUTIONS_RF,
    PARAM_DISTRIBUTIONS_XG,
)

from app.preprocessing.pipeline import build_preprocessor

import mlflow
import joblib
from xgboost import XGBClassifier



def track_experiment(model_name, search_file):

    with mlflow.start_run(run_name=f"{model_name}_tuning"):

        mlflow.set_tag("experiment_type", "hyperparameter_tuning")
        mlflow.set_tag("model", model_name)

        results = search_file.cv_results_

        for i, params in enumerate(results["params"]):
            
            with mlflow.start_run(
                run_name=f"{model_name}_candidate_{i + 1}",
                nested=True
                ):
                
                mlflow.log_params(params)

                mlflow.log_metric(
                    "mean_cv_f1",
                    results["mean_test_score"][i]
                )

                mlflow.log_metric(
                "std_cv_f1",
                    results["std_test_score"][i]
                )

                mlflow.log_metric(
                "rank",
                    results["rank_test_score"][i]
                )

        mlflow.log_params(search_file.best_params_)
        mlflow.log_metric("best_cv_f1", search_file.best_score_)
    

def evaluate_best_candidate(model_name, search_file, x_test, y_test, encoder=None):

    with mlflow.start_run(run_name=f"Tuned_{model_name}"):

        y_pred = search_file.predict(x_test)

        if encoder is not None:
            y_pred = encoder.inverse_transform(y_pred)
            mlflow.log_artifact(LABEL_ENCODER_OUTPUT_PATH)

        mlflow.log_params(search_file.best_params_)

        # Calculate metrics
        evaluation = evaluate_model(
            y_test = y_test, 
            y_pred = y_pred, 
            confusion_matrix_path = f"training/artifacts/confusion_matrix_tuned_{model_name}.png",
            classification_report_path= f"training/artifacts/classification_report_tuned_{model_name}.txt"
            )

        mlflow.log_metrics(evaluation)


        # Log artifacts
        mlflow.log_artifact(
            f"models/model_tuned_{model_name}.joblib"
            )
        mlflow.log_artifact(
            PREPROCESSOR_OUTPUT_PATH
            )
        mlflow.log_artifact(
            f"training/artifacts/confusion_matrix_tuned_{model_name}.png"
            )
        mlflow.log_artifact(
            f"training/artifacts/classification_report_tuned_{model_name}.txt"
            )



def experiment_model_selection():
    '''
    Execute the experiment reported in docs\Hyperparameter_tuning_strategy.md

    '''

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
    X_test_transformed = preprocessor.transform(X_test)

    joblib.dump(
        preprocessor,
        PREPROCESSOR_OUTPUT_PATH,
        )

    #---------------------------------   
    # ------------Random Forest experiment
    #---------------------------------   

    model_RF = RandomForestClassifier(random_state=RANDOM_SEED)
    model_name_RF = RANDOM_FOREST
    search_RF = tune_model(
        model=model_RF,
        param_distributions=PARAM_DISTRIBUTIONS_RF,
        X_train=X_train_transformed,
        y_train=y_train
        )

    joblib.dump(
        search_RF.best_estimator_,
        f"models/model_tuned_{model_name_RF}.joblib",
        )
   
    track_experiment(model_name_RF, search_RF)

    evaluate_best_candidate(
        model_name_RF,
        search_RF,
        X_test_transformed,
        y_test
        )

    
    #---------------------------------   
    #----------------XGBoost
    #---------------------------------   
   
    encoder, y_train_encoded = fit_label_encoder(y_train)
 
    joblib.dump(
        encoder,
        LABEL_ENCODER_OUTPUT_PATH,
        )

    model_XGBoost = XGBClassifier(
        random_state=RANDOM_SEED)
    model_name_XG = XGBOOST

    search_XG = tune_model(
        model=model_XGBoost,
        param_distributions=PARAM_DISTRIBUTIONS_XG,
        X_train=X_train_transformed,
        y_train=y_train_encoded,
        )
    
    joblib.dump(
        search_XG.best_estimator_,
        f"models/model_tuned_{model_name_XG}.joblib",
        )
    
    track_experiment(model_name_XG, search_XG)

    evaluate_best_candidate(model_name_XG, search_XG, X_test_transformed, y_test, encoder=encoder)

   



if __name__ == "__main__":
    experiment_model_selection()


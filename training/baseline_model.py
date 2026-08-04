from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from training.config import (
    RANDOM_SEED,
    MAX_ITERATIONS,
    MODEL_NAME,
    CRITERION,
    N_ESTIMATORS,
    LOGISTIC_REGRESSION,
    RANDOM_FOREST,
    XGBOOST,
    XGB_MAX_DEPTH,
    XGB_LEARNING_RATE,
    XGB_SELECTED_LEARNING_RATE,
    XGB_SELECTED_N_ESTIMATORS,
    XGB_SELECTED_MAX_DEPTH,
    XGB_SELECTED_SUBSAMPLE,
    XGB_SELECTED_COLSAMPLE,
)

def build_model():
    if MODEL_NAME == LOGISTIC_REGRESSION:
        return LogisticRegression(
            random_state=RANDOM_SEED,
            max_iter=MAX_ITERATIONS
        )
    elif MODEL_NAME == RANDOM_FOREST:
        return RandomForestClassifier(
            random_state=RANDOM_SEED, 
            criterion=CRITERION,
            n_estimators=N_ESTIMATORS,
        )
    elif MODEL_NAME == XGBOOST:
        return XGBClassifier(
            random_state=RANDOM_SEED,
            max_depth=XGB_MAX_DEPTH,
            learning_rate=XGB_LEARNING_RATE,
        )
    else:
        raise ValueError(
        f"Unsupported model '{MODEL_NAME}'."
    )

def build_selected_xgboost():
    return XGBClassifier(
                random_state=RANDOM_SEED,
                n_estimators = XGB_SELECTED_N_ESTIMATORS,
                max_depth=XGB_SELECTED_MAX_DEPTH,
                learning_rate=XGB_SELECTED_LEARNING_RATE,
                subsample=XGB_SELECTED_SUBSAMPLE,
                colsample_bytree=XGB_SELECTED_COLSAMPLE,
        )







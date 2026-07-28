from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from training.config import (
    RANDOM_SEED,
    MAX_ITERATIONS,
    MODEL_NAME,
    CRITERION,
    N_ESTIMATORS,
    LOGISTIC_REGRESSION,
    RANDOM_FOREST,
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
    
    else:
        raise ValueError(
        f"Unsupported model '{MODEL_NAME}'."
    )





from sklearn.linear_model import LogisticRegression

from training.config import (
    RANDOM_SEED,
    MAX_ITERATIONS,
)

def build_baseline_model():

    return LogisticRegression(
        random_state=RANDOM_SEED,
        max_iter=MAX_ITERATIONS
    )


from sklearn.model_selection import RandomizedSearchCV

from training.config import (
    N_ITER,
    CV,
    SCORING,
    RANDOM_SEED,
)

def tune_model(model, param_distributions, X_train, y_train, n_iterations=N_ITER):

    search = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_distributions,
        n_iter=n_iterations,
        cv=CV,
        scoring=SCORING,
        random_state=RANDOM_SEED,
        n_jobs=-1,
    )

    search.fit(X_train, y_train)

    return search
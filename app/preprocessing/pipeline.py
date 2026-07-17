# Contains the build_preprocessor() function

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from app.preprocessing.features import (
    NUMERICAL_FEATURES,
    BINARY_FEATURES,
)
from app.preprocessing.config import (
    NUMERICAL_SCALER,
    RANDOM_SEED,
)


def build_preprocessor() -> ColumnTransformer:
    """
    Build the preprocessing pipeline used during
    both model training and inference.

    Returns
    -------
    ColumnTransformer
        Configured preprocessing pipeline.
    """
    
    # Numerical feature transformation
    numeric_transformer = Pipeline([
        ("scaler", NUMERICAL_SCALER)
    ])

    # Binary features are already encoded as 0/1, so they are passed through unchanged.
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                numeric_transformer,
                NUMERICAL_FEATURES,
            ),
            (
                "bin",
                "passthrough",
                BINARY_FEATURES,
            ),
        ]
    )

    return preprocessor

if __name__=='__main__':
    preprocessor = build_preprocessor()

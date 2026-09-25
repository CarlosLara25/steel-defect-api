import pandas as pd

from training.config import (
    TARGET_CLASSES,
    DATASET_PATH,
    FEATURES,
)

def validate_target_encoding(targets: pd.DataFrame) -> None:

    only_binary = targets.isin([0, 1]).all().all()
    one_positive = (targets.sum(axis=1) == 1).all() 

    if not (only_binary and one_positive):
        raise ValueError(
            "Invalid target encoding. Each sample must contain exactly one class encoded as 1 and all remaining classes encoded as 0."
        )


def load_training_data() -> tuple[pd.DataFrame, pd.Series]:

    '''
    Load the training dataset, validate one-hot encoded target,
    convert it into a single target series, and 
    return the feature matrix (X) and target vector (y).
    
    '''

    df = pd.read_csv(DATASET_PATH, sep='\t', keep_default_na=False, header=None, names=FEATURES+TARGET_CLASSES)    

    expected_columns = FEATURES + TARGET_CLASSES
    if list(df.columns) != expected_columns:
        raise ValueError("Unexpected dataset structure.")

    X = df[FEATURES]
    targets = df[TARGET_CLASSES]

    validate_target_encoding(targets)
    
    y = targets.idxmax(axis=1)
    y.name = "target"    
    
    return X, y





from sklearn.compose import ColumnTransformer

from app.preprocessing.pipeline import build_preprocessor

import pandas as pd

import numpy as np

import pytest

def test_build_preprocessor_return_column_transfromer():
    """
    Verify that the preprocessing pipeline is built successfully.
    """
    preprocessor = build_preprocessor()

    assert isinstance(preprocessor, ColumnTransformer)


# Ensure our architecture remains intact
def test_preprocessor_contains_expected_transformers():
    preprocessor = build_preprocessor()

    transformer_names = [
        name
        for name, _, _ in preprocessor.transformers
    ]

    assert "num" in transformer_names
    assert "bin" in transformer_names

#Ensure fit and transform works with a synthetic dataframe, and shape is conserved
def test_preprocessor_functional_check(sample_data):
    
    preprocessor = build_preprocessor()
    preprocessor.fit(sample_data)

    transformed = preprocessor.transform(sample_data)

    assert transformed.shape == (3, 27)

# Ensure the binary variables passthrough
def test_preprocessor_binary_passtrhough(sample_data):
    
    preprocessor = build_preprocessor()
    preprocessor.fit(sample_data)

    transformed = preprocessor.transform(sample_data)

    transformed_df = pd.DataFrame(
    transformed,
    columns=preprocessor.get_feature_names_out()
    )


    np.testing.assert_array_equal(
        transformed_df["bin__TypeOfSteel_A300"],
        sample_data["TypeOfSteel_A300"],
    )

    np.testing.assert_array_equal(
        transformed_df["bin__TypeOfSteel_A400"],
        sample_data["TypeOfSteel_A400"],
    )

def test_preprocessor_missing_column(sample_data):
    sample = sample_data.drop(columns=["Log_Y_Index"])
    
    preprocessor = build_preprocessor()

    with pytest.raises(ValueError):
        preprocessor.fit(sample)
    
def test_preprocessor_wrong_datatype(sample_data):
    sample_data["Log_Y_Index"] = "String sample"
    
    preprocessor = build_preprocessor()
    
    with pytest.raises(ValueError):
        preprocessor.fit(sample_data)

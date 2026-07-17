from sklearn.compose import ColumnTransformer

from app.preprocessing.pipeline import build_preprocessor

import pandas as pd
import numpy as np

import pytest

@pytest.fixture
def sample_data():
    return  pd.DataFrame(
    {
        "X_Minimum": [10, 20, 30],
        "X_Maximum": [40, 50, 60],
        "Y_Minimum": [1000, 1200, 1300],
        "Y_Maximum": [1010, 1220, 1330],
        "Pixels_Areas": [250, 260, 270],
        "X_Perimeter": [10, 12, 14],
        "Y_Perimeter": [30, 40, 50],
        "Sum_of_Luminosity": [20000, 23000, 27000],
        "Minimum_of_Luminosity": [80, 90, 110],
        "Maximum_of_Luminosity": [110, 120, 130],
        "Length_of_Conveyer": [1000, 1500, 2000],
        "TypeOfSteel_A300": [0, 0, 1],
        "TypeOfSteel_A400": [1, 1, 0],
        "Steel_Plate_Thickness": [90, 120, 130],
        "Edges_Index": [0.10, 0.20, 0.30],
        "Empty_Index": [0.35, 0.40, 0.50],
        "Square_Index": [0.10, 0.20, 0.150],
        "Outside_X_Index": [0.010, 0.020, 0.030],
        "Edges_X_Index": [0.50, 0.60, 0.70],
        "Edges_Y_Index": [1.0, 0.95, 0.90],
        "Outside_Global_Index": [0, 0.5, 1],
        "LogOfAreas": [2.3, 2.0, 3.0],
        "Log_X_Index": [1.0, 1.20, 1.30],
        "Log_Y_Index": [1.35, 1.70, 1.90],
        "Orientation_Index": [0.60, 0.70, 0.80],
        "Luminosity_Index": [-0.270, -0.120, 0.030],
        "SigmoidOfAreas": [0.40, 0.70, 0.95]
    })



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

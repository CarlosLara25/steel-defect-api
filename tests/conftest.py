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


@pytest.fixture
def unique_sample_data(sample_data):
    return  sample_data.iloc[0].to_dict()
    





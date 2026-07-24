
RANDOM_SEED = 42

MAX_ITERATIONS = 1000

TEST_SIZE = 0.2

TARGET_CLASSES = [
    "Pastry",
    "Z_Scratch",
    "K_Scatch",
    "Stains",
    "Dirtiness",
    "Bumps",
    "Other_Faults"
]

FEATURES = [
    "X_Minimum",
    "X_Maximum",
    "Y_Minimum",
    "Y_Maximum",
    "Pixels_Areas",
    "X_Perimeter",
    "Y_Perimeter",
    "Sum_of_Luminosity",
    "Minimum_of_Luminosity",
    "Maximum_of_Luminosity",
    "Length_of_Conveyer",
    "TypeOfSteel_A300",
    "TypeOfSteel_A400",
    "Steel_Plate_Thickness",
    "Edges_Index",
    "Empty_Index",
    "Square_Index",
    "Outside_X_Index",
    "Edges_X_Index",
    "Edges_Y_Index",
    "Outside_Global_Index",
    "LogOfAreas",
    "Log_X_Index",
    "Log_Y_Index",
    "Orientation_Index",
    "Luminosity_Index",
    "SigmoidOfAreas"
]

DATASET_PATH ="data/raw/Faults.NNA"

PREPROCESSOR_OUTPUT_PATH = "models/preprocessor.joblib"
MODEL_OUTPUT_PATH = "models/model.joblib"
CONFUSION_MATRIX_PATH = "training/artifacts/confusion_matrix.png"
CLASSIFICATION_REPORT_PATH = "training/artifacts/classification_report.txt"

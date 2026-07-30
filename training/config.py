

# -----  logistic regression
LOGISTIC_REGRESSION = "logistic_regression"
MAX_ITERATIONS = 1000


#-------- random forest
RANDOM_FOREST = "random_forest" 
CRITERION = "gini"
N_ESTIMATORS = 100

#----------xgboost
XGBOOST = "xgboost"
XGB_MAX_DEPTH = 10
XGB_LEARNING_RATE = 0.3

#-----------General
TEST_SIZE = 0.2
RANDOM_SEED = 42

MODEL_NAME = XGBOOST

#---------model selection
#---------RandomizedSearchCV
N_ITER = 20
CV = 5
SCORING = "f1_macro"


#----------------Classes
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
MODEL_OUTPUT_PATH = f"models/model_{MODEL_NAME}.joblib"
CONFUSION_MATRIX_PATH = f"training/artifacts/confusion_matrix_{MODEL_NAME}.png"
CLASSIFICATION_REPORT_PATH = f"training/artifacts/classification_report_{MODEL_NAME}.txt"
LABEL_ENCODER_OUTPUT_PATH = f"models/label_encoding.joblib"
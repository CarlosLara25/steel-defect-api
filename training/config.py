
#-----------General
TEST_SIZE = 0.2
RANDOM_SEED = 42


# Experiments----------------------------------

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

#--------------- Model selected to train in experiment
MODEL_NAME = XGBOOST

# -------------- PATHS
PREPROCESSOR_OUTPUT_PATH = "models/experiments/preprocessor.joblib"
MODEL_OUTPUT_PATH = f"models/experiments/model_{MODEL_NAME}.joblib"
CONFUSION_MATRIX_PATH = f"training/artifacts/confusion_matrix_{MODEL_NAME}.png"
CLASSIFICATION_REPORT_PATH = f"training/artifacts/classification_report_{MODEL_NAME}.txt"
LABEL_ENCODER_OUTPUT_PATH = f"models/experiments/label_encoding.joblib"

#---------------------------------------------------
# model selection
#---------------------------------------------------

#---------RandomizedSearchCV
N_ITER = 20
CV = 5
SCORING = "f1_macro"


#-----------XGBoost_selected_configuration
MODEL_TYPE = XGBOOST
VERSION_MODEL = "1.0.0"
XGB_SELECTED_LEARNING_RATE = 0.03
XGB_SELECTED_N_ESTIMATORS = 700
XGB_SELECTED_MAX_DEPTH = 9
XGB_SELECTED_SUBSAMPLE = 0.6
XGB_SELECTED_COLSAMPLE = 0.9
XGB_SELECTION_METRIC = "macro_f1"
XGB_CV_MACRO_F1 = 0.8268
XGB_TEST_MACRO_F1 = 0.8227

PREPROCESSOR_OUTPUT_PATH_SELECTED = "models/selected/preprocessor.joblib"
MODEL_OUTPUT_PATH_SELECTED = f"models/selected/model_{MODEL_NAME}_{VERSION_MODEL}.joblib"
CONFUSION_MATRIX_PATH_SELECTED = f"training/artifacts/confusion_matrix_{MODEL_NAME}_{VERSION_MODEL}.png"
CLASSIFICATION_REPORT_PATH_SELECTED = f"training/artifacts/classification_report_{MODEL_NAME}_{VERSION_MODEL}.txt"
LABEL_ENCODER_OUTPUT_PATH_SELECTED = f"models/selected/label_encoding_{MODEL_NAME}_{VERSION_MODEL}.joblib"
METADATA_PATH_SELECTED = f"models/selected/metadata_{MODEL_NAME}_{VERSION_MODEL}.json"


#----------------Dataset and Classes

DATASET_PATH ="data/raw/Faults.NNA"

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

#-----------------------------------



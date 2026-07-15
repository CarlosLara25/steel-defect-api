
## Objective

> Define the preprocessing strategy for Version 1 of the machine learning pipeline based on the findings of the Exploratory Data Analysis (EDA). The resulting preprocessing pipeline must be reusable during both model training and inference.

## Current Transformations


| Transformation      | Decision              | Reason                                                               | Source               |
| ------------------- | --------------------- | -------------------------------------------------------------------- | -------------------- |
| Missing values      | Reject requests containing missing values | Dataset contains no missing values and all 27 features are required. The API should return an error rather than silently imputing values. | EDA + FR-007         |
| Duplicate removal   | None                  | No duplicates found.                                                 | EDA                  |
| Binary features     | Keep unchanged        | Already encoded as 0/1.                                              | EDA                  |
| Numerical scaling   | StandardScaler        | Good baseline for comparing algorithms.                              | Engineering Decision |
| Outlier removal     | None                  | Preserve potentially informative defect samples.                     | EDA                  |
| Feature selection   | None                  | Evaluate after baseline.                                             | Engineering Decision |
| Feature engineering | None                  | Keep baseline simple.                                                | Engineering Decision |


## Deferred Transformations

We are currently deferring these transformations:

- PCA
- Feature selection
- SMOTE
- Outlier removal
- Feature engineering

These transformations are intentionally excluded from Version 1 to establish a simple and reproducible baseline before introducing additional complexity.

## Design Decisions

### Scikit-Learn Pipeline

The preprocessing workflow will be implemented using Scikit-Learn Pipelines because they are:

- reusable
- serializable
- easy to test
- compatible with production deployment
- industry standard

### ColumnTransformer

ColumnTransformer will be used to apply different preprocessing steps to numerical and binary features.

- Numerical features → StandardScaler
- Binary features → passthrough

## Scope

Version 1 of the preprocessing pipeline will include:

- Input validation
- Numerical feature scaling
- Binary feature passthrough

Version 1 will not include:

- Missing-value imputation
- Outlier removal
- Feature engineering
- Feature selection
- Dimensionality reduction

## Open Questions

- Should RobustScaler be evaluated as an alternative to StandardScaler?
- Should correlated features be removed after baseline evaluation?
- Should extreme observations be treated differently if they negatively affect model performance?

## Input Validation Note

Input validation is handled before the preprocessing transformations. This separates data validation (ensuring requests are valid) from data transformation (preparing valid data for the model).

Input validation decisions:

- All 27 features are mandatory, consequently, missing values should be rejected.
- Binary features should remain 0/1.


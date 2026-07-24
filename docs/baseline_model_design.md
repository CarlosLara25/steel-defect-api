## 1. Objective

Build a reproducible baseline classification model for the Steel Plates Faults dataset. The objective is to establish an initial performance reference and produce artifacts that can later be deployed through the FastAPI inference service.

## 2. Dataset


**Dataset name:** 
  Steel Plates Faults by UCI MAchine Learning Repository

**Number of Samples:**  1941

**Number of Features:** 27

**Number of Classes**: 7

## 3. Data split

**Training:** 80%

**Testing:** 20%

**Random State** = 42

**Stratified split** 
    
- **Decision:** Yes

- **Reason**: Stratified splitting preserves the class distribution in both subsets.


## 4. Preprocessing

- Numerical features standardized using StandardScaler.
- Binary features passed through unchanged.
- Preprocessing fitted only on the training set to avoid data leakage.

## 5. Baseline model selection


Candidate models

| Model               | Advantages          | Disadvantages |
| ------------------- | ------------------- | ------------- |
| Logistic Regression | Fast, interpretable | Linear        |
| Random Forest       | Non-linear          | Larger model  |
| XGBoost             | High performance    | More complex  |

### Selection:

Logistic Regression is selected as the baseline because it provides a simple, reproducible, and interpretable reference for future comparisons.


## 6. Evaluation metrics

For a multiclass classification problem:

- Accuracy
- Precision (macro)
- Recall (macro)
- F1-score (macro)
- Confusion Matrix


## 7. Artifacts

```
models/
    preprocessor.joblib
    logistic_regression.joblib
```    
    
## 8. MLflow logging

### Parameters:

- solver
- random_state
- max_iter

### Metrics:

- accuracy
- precision
- recall
- f1

### Artifacts:

- model
- preprocessor
- confusion matrix

## 9. Future improvements

- Hyperparameter optimization
- Feature selection
- Class imbalance techniques
- Random Forest comparison
- XGBoost evaluation
- Cross-validation
- Probability calibration

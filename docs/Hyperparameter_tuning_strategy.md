# Hyperparameter Tuning Strategy

## Objective

Improve the Macro F1-score of the Random Forest
and XGBoost candidate models.

## Candidate Models

- Random Forest
- XGBoost

## Primary Selection Metric

Macro F1-score.

## Cross-Validation

Stratified K-Fold cross-validation with 5 folds will be used.

The same folds and random state will be used for both candidate models
to improve comparability.

- Number of folds: 5
- Stratification: Yes
- Shuffle: Yes
- Random state: RANDOM_SEED

## Search Strategy

- RandomizedSearchCV will be used to explore the
hyperparameter space.
- n_iter=20 per model, resulting 40 sampled configurations across both models.

## Random Forest

| Hyperparameter | Search space |
|---|---|
| n_estimators | 100, 200, 300, 500 |
| max_depth | None, 10, 20, 30 |
| min_samples_split | 2, 3, 4, 5, 6, 7 |
| max_features | sqrt, log2 |

### Fixed hyperparameters

| Hyperparameter | value |
|-------|-----|
| min_samples_leaf | default=1 |
|criterion|"gini"|

## XGBoost

| Hyperparameter | Search space |
|---|---|
| n_estimators | 100, 200, 300, 500 |
| learning_rate | 0.01, 0.03, 0.06, 0.1, 0.2, 0.3, 0.4 |
| max_depth | 4, 7, 10, 13 |
| subsample | 0.5, 0.7, 1.0 |
| colsample_bytree | 0.7, 0.8, 1.0 |

### Fixed hyperparameters
| Hyperparameter | value |
|-------|-----|
| min_split_loss | default=0 |
| reg_alpha | default=0 |
| reg_lambda | default=1 |
| tree_method | default=auto |

## Selection Criteria


### Hyperparameter selection

Within each model family, the best hyperparameter configuration will be
selected according to mean cross-validated Macro F1.

### Final model selection

The tuned Random Forest and XGBoost models will then be evaluated on the
held-out test set.

The final model will be selected primarily according to Macro F1, with
per-class recall and the confusion matrix considered as secondary criteria,
particularly for the minority defect classes.


## Tracking Strategy

MLflow will be used to track the hyperparameter tuning experiments.

For each model:

- A parent MLflow run will represent the hyperparameter search.
- Each sampled hyperparameter configuration will be tracked as a nested run.
- Each candidate run will record:
  - Hyperparameters
  - Mean cross-validation Macro F1
  - Standard deviation of cross-validation Macro F1
  - Candidate rank

The best configuration identified by RandomizedSearchCV will be recorded in
the parent run.

The selected configuration will then be retrained using the complete training
set and evaluated once on the held-out test set.

A separate final MLflow run will record:

- Selected hyperparameters
- Cross-validation Macro F1
- Test metrics
- Classification report
- Confusion matrix
- Final model artifact
- Preprocessor artifact

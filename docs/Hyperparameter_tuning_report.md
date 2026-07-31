## Hyperparameter tuning analysis

### Experiment

Strategy documentation:

[`Hyperparameter_tuning_strategy.md`](Hyperparameter_tuning_strategy.md)

Code file:

[`training\experiment_orchestration.py`](..\training\experiment_orchestration.py)


## Results


### Model
Random Forest

### Parameters

|Parameter |Value|
|--|--|
|n_estimators|200|
|min_samples_split|4|
|max_features|sqrt|
|max_depth|None|

### Metrics

|Metric| Value|
|--|--|
|accuracy|0.8072|
|precision|0.8475|
|recall|0.7718|
|f1|0.8041|

### Model
XGBoost

### Parameters

|Parameter |Value|
|--|--|
|subsample| 0.7|
|n_estimators|100|
|max_depth|10|
|learning_rate|0.1|
|colsample_bytree|1.0|

### Metrics
|Metric| Value|
|--|--|
|accuracy|0.8072|
|precision|0.8481|
|recall|0.8138|
|f1|0.8295|

### Comparison of tuning results

Reults of the experiment:

|Metric| RF| XGBoost|  
|--|--|--|
|best_cv_f1|0.7972|0.8218


Results on the held-out test set:

|Metric| RF| XGBoost|  
|--|--|--|
|accuracy|0.8072|0.8072|
|precision|0.8475|**0.8481**|
|recall|0.7718|**0.8138**|
|f1|0.8041|**0.8295**|


The tuned XGBoost model achieved higher cross-validated Macro F1 and higher test-set Macro F1 than the tuned Random Forest. Although both models achieved the same accuracy on the held-out test set, XGBoost achieved higher macro precision and substantially higher macro recall, resulting in a higher Macro F1-score. Therefore, XGBoost will be retained as the sole candidate for further tuning.

### XGBoost Experiment Analysis

The top-performing configurations were analyzed to identify promising
regions of the hyperparameter space for a second tuning experiment.

#### n_estimators

The top five candidates used `n_estimators` values of 100 or 500.
The intermediate values 200 and 300 were not represented among the top five configurations.

#### learning_rate

The top five candidates used learning rates between 0.01 and 0.1.
Higher values (0.2, 0.3, and 0.4) were not represented among the top-performing configurations.

#### max_depth

The top five candidates used `max_depth` values of 7 or 10,
suggesting that this region may be more promising than the lower or higher values evaluated in the first experiment.

#### subsample

The top five candidates used `subsample` values of 0.5 or 0.7. The value 1.0 was not represented among the top-performing configurations.

#### colsample_bytree

The top five candidates used `subsample` values of 0.7, 0.8 or 1.0. The full set of values is represented among the top-performing configurations.

### Proposed Next Experiment

The second experiment will focus the XGBoost search around the regions identified from the first experiment. The search space will be refined to increase resolution in promising regions.

| Hyperparameter | Search space |
|---|---|
| n_estimators | 100, 300, 500, 700 |
| learning_rate | 0.01, 0.03, 0.05, 0.07, 0.10, 0.13, 0.15 |
| max_depth | 7, 9, 11 |
| subsample | 0.4, 0.5, 0.6, 0.7, 0.8 |
| colsample_bytree | 0.7, 0.8, 0.9, 1.0 |

`RandomizedSearchCV` will be used with `n_iter=40` and 5-fold
Stratified Cross-Validation, using Macro F1 as the primary optimization metric.


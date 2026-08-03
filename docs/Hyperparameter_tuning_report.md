# Hyperparameter tuning analysis

## 1. Experiment 1 - Model Tuning

Strategy documentation:

[`Hyperparameter_tuning_strategy.md`](Hyperparameter_tuning_strategy.md)

Code file:

[`training\experiment_orchestration.py`](..\training\experiment_orchestration.py)


### Random Forest

 

#### Best Candidate Parameters: 


|Parameter |Value|
|--|--|
|n_estimators|200|
|min_samples_split|4|
|max_features|sqrt|
|max_depth|None|

#### Held-out Test Metrics:

|Metric| Value|
|--|--|
|accuracy|0.8072|
|precision|0.8475|
|recall|0.7718|
|f1|0.8041|


### XGBoost

#### Best Candidate Parameters: 
|Parameter |Value|
|--|--|
|subsample| 0.7|
|n_estimators|100|
|max_depth|10|
|learning_rate|0.1|
|colsample_bytree|1.0|

#### Held-out Test Metrics:
|Metric| Value|
|--|--|
|accuracy|0.8072|
|precision|0.8481|
|recall|0.8138|
|f1|0.8295|

### Comparison of tuning results

#### Results of the experiment:

|Metric| RF| XGBoost|  
|--|--|--|
|best_cv_f1|0.7972|0.8218

#### Results on the held-out test set:

|Metric| RF| XGBoost|  
|--|--|--|
|accuracy|0.8072|0.8072|
|precision|0.8475|**0.8481**|
|recall|0.7718|**0.8138**|
|f1|0.8041|**0.8295**|


### Conclusion
The tuned XGBoost model achieved higher cross-validated Macro F1 and higher test-set Macro F1 than the tuned Random Forest. Although both models achieved the same accuracy on the held-out test set, XGBoost achieved higher macro precision and substantially higher macro recall, resulting in a higher Macro F1-score. Therefore, XGBoost will be retained as the sole candidate for further tuning.

## 2. Experiment 2 - XGBoost Refinement 

### Motivation

The top-performing configurations were analyzed to identify promising
regions of the hyperparameter space for a second tuning experiment.

- **n_estimators**: The top five candidates used `n_estimators` values of 100 or 500.
The intermediate values 200 and 300 were not represented among the top five configurations.

- **learning_rate**: The top five candidates used learning rates between 0.01 and 0.1.
Higher values (0.2, 0.3, and 0.4) were not represented among the top-performing configurations.

- **max_depth**: The top five candidates used `max_depth` values of 7 or 10,
suggesting that this region may be more promising than the lower or higher values evaluated in the first experiment.

- **subsample**: The top five candidates used `subsample` values of 0.5 or 0.7. The value 1.0 was not represented among the top-performing configurations.

- **colsample_bytree**:
The top five candidates used `colsample_bytree` values of 0.7, 0.8 or 1.0. The full set of values is represented among the top-performing configurations.

These observations, together with the results of the first experiment, motivated a second experiment with a refined search space focused on promising regions.

### Search Space

The second experiment will focus the XGBoost search around the regions identified from the first experiment. 

| Hyperparameter | Search space |
|---|---|
| n_estimators | 100, 300, 500, 700 |
| learning_rate | 0.01, 0.03, 0.05, 0.07, 0.10, 0.13, 0.15 |
| max_depth | 7, 9, 11 |
| subsample | 0.4, 0.5, 0.6, 0.7, 0.8 |
| colsample_bytree | 0.7, 0.8, 0.9, 1.0 |

`RandomizedSearchCV` will be used with `n_iter=50` and 5-fold
Stratified Cross-Validation, using Macro F1 as the primary optimization metric.

### Results

The best candidate achieved a cross-validated Macro F1 of
0.8268.

Results on the held-out test set:

|Metric| refined_XGBoost|  
|--|--|
|accuracy|0.8046|
|precision|0.8340|
|recall|0.8127|
|f1|0.8227|


### Top Candidates

The top 7 candidates based on the score **best_cv_f1** are presented in the following table.

|Top| best_cv_f1 |colsample_bytree|learning_rate|max_depth|n_estimators|subsample|
|--|--|--|--|--|--|--|
|1|0.8268|0.9|0.03|9|700|0.6|
|2|0.8258|0.8|0.03|9|700|0.7
|3|0.8249|1.0|0.03|9|500|0.7
|4|0.8243|0.8|0.05|11|300|0.8
|5|0.8222|0.9|0.13|9|100|0.8
|6|0.8216|0.9|0.15|7|300|0.8
|7|0.8213|0.7|0.03|9|700|0.8



### Hyperparameter Analysis

Mild tendencies can be observed among the candidates in relation with the hyperparameters:
- **Most frequent hyperparameter values:** The most frequent values among the top seven candidates were `learning_rate=0.03` (5/7), `max_depth=9` (5/7), and `subsample=0.8` (4/7).
- **Full search-space coverage:** The top seven candidates collectively cover the complete search space for ``n_estimators``, ``max_depth``, and ``colsample_bytree``. 
- The top 1, 2, and 7 candidates **share the same values for learning_rate=0.03, max_depth=9, and n_estimators=700,** while differing in subsample and colsample_bytree

### Comparison with Experiment 1

| Metric | Experiment 1 | Experiment 2 |
|---|---:|---:|
| Best CV Macro F1 | 0.8218 | **0.8268** |
| Test Macro F1 | **0.8295** | 0.8227 |

### Conclusion

Although some concentrations are visible, the top candidates do not define a sufficiently narrow and consistent region to justify another manually narrowed search. In particular, n_estimators, max_depth, and colsample_bytree span their complete search spaces among the top candidates, while learning_rate and subsample still cover multiple values. Furthermore, although Experiment 2 improved the best cross-validation Macro F1 from 0.8218 to 0.8268, its selected configuration achieved a lower Macro F1 on the held-out test set (0.8227 vs. 0.8295).

### Stopping Decision:
No further manual refinement experiment is recommended. Experiment 2 improved the best CV Macro F1 but did not improve the held-out test performance, and the top candidates did not identify a sufficiently narrow and consistent region for another manually defined search space.

## 3. Final Model Candidate

Based on the predefined primary selection metric, cross-validated Macro F1, the XGBoost configuration with the highest CV Macro F1 was selected as the final model candidate. The held-out test set was used only for final performance evaluation and was not used for hyperparameter selection.

### Selected Model
XGBoost

### Selected Hyperparameters

| Hyperparameter | value |
|---|---|
| n_estimators | 700
| learning_rate | 0.03
| max_depth | 9
| subsample | 0.6
| colsample_bytree | 0.9

### Fixed hyperparameters
| Hyperparameter | value |
|-------|-----|
| min_split_loss | default=0 |
| reg_alpha | default=0 |
| reg_lambda | default=1 |
| tree_method | default=auto |

### Performance

| Metric | selected model
|---|---:|
| Best CV Macro F1 |  0.8268 |
| Test Macro F1 |  0.8227 |



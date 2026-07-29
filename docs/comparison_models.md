## Models Comparison

| model | accuracy |      precision macro  |  recall macro | f1-score macro |f1-score weighted|  note|
|--------|--------|-----------|---------|----------|---|-----|
|logistic regression  | 0.72  |    0.76  |    0.73   |   0.74   | 0.72 |  baseline|
|random forest  | 0.80  |   **0.85**   |   0.79   |   **0.82**   | 0.80 |    candidate|
|XGBoost    |  **0.81**   |  0.82   |   **0.81**   |  0.81  |  **0.81** | candidate |

## Conclusion 
Logistic Regression established the initial baseline. Random Forest and XGBoost both provided substantial improvements. Random Forest achieved the highest Macro F1-score (0.82), while XGBoost obtained the highest overall accuracy (0.81), weighted F1-score (0.81), and macro recall (0.81). Since the performance difference between the two tree-based models is small, both were selected as candidates for the subsequent hyperparameter tuning stage.
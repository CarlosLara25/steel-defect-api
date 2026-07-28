## Models Comparison

| model | accuracy |      precision macro  |  recall macro | f1-score macro |f1-score weighted|  note|
|--------|--------|-----------|---------|----------|---|-----|
|logistic regression  | 0.72  |    0.76  |    0.73   |   0.74   | 0.72 |  baseline|
|random forest  | 0.80  |   0.85   |   0.79   |   0.82   | 0.80 |    current best|
|XGboost    |  -   |  -   |   -   |  -  |  - |planned|


Macro F1 was selected as the primary evaluation metric because the dataset is imbalanced and the objective is to achieve good performance across all seven defect classes rather than favoring the most frequent defects.

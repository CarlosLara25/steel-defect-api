
# logistic regression

## Description

Model evaluated as promissing for its known High performance and accuracy, particularly with structured data. 

### Library:
xgboost.XGBClassifier

### Basic hyperparameters:

- random_state=42
- max_depth=10
- learning_rate=0.3


## Results


### Classification report: 
| index | failure |       precision  |  recall | f1-score |  support|
|---|--------|-------------------|---------|----------|--------|
| 0 |Bumps    |   0.76    |  0.68  |    0.72  |      81  |
| 1 |Dirtiness |    0.75    |  0.82  |    0.78  |      11  |
| 2 |K_Scatch   |  0.99   |   0.95  |    0.97   |     78  |
| 3 |Other_Faults |      0.74   |   0.81   |   0.77    |   135  |
| 4 |Pastry    |   0.56   |   0.59  |    0.58    |    32  |
| 5 |Stains   |    0.92   |   0.86  |    0.89    |    14  |
| 6 |Z_Scratch   |    1.00   |   0.95  |    0.97    |    38  |
|

#### Global:

**accuracy:**  0.81 

| avg |       precision  |  recall | f1-score |  support|
|--------|-------------------|---------|----------|--------|
|macro    |   0.82   |   0.81   |   0.81   |    389|
|weighted   |    0.81   |   0.81   |   0.81   |    389|


### Confusion matrix

![Confusion_matrix](../training/artifacts/confusion_matrix_xgboost.png)


## Conclusion 

The xgboost model without hyperaparameters tunning achieved an overall accuracy of 0.81 and a macro F1-score of 0.81, surpassing in both metrics to the reference model.

Performance varied across defect categories. Both K_Scratch, and Z_Scratch (F1 = 0.97) were classified with high reliability, suggesting that the available numerical descriptors effectively separate these defect types.

The lowest performance was observed for the Pastry class (F1 = 0.58), followed by Bumps (F1 = 0.72). Analysis of the confusion matrix reveals that both classes are frequently misclassified as Other_Faults. Likewise, samples belonging to Other_Faults are often predicted as Bumps or Pastry, indicating a bidirectional confusion among these three categories.

Altough the results indicate an improving respect to the baseline, still misclassifications occur consistently. Class imbalance may contribute to the difficulty, but it does not fully explain it. The confusion between Pastry, Bumps, and Other_Faults is likely also driven by the similarity of their feature distributions.Then, tuning of hyperparameters is required.

 
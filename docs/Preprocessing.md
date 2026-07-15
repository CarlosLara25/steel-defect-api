
## Objective

Take decisions of the required preprocessing transformations and the tools used for their implementation.

## Current Transformations


| Transformation      | Decision           | Reason                                               |
| ------------------- | ------------------ | ---------------------------------------------------- |
| Missing values      | None               | EDA. Dataset has no missing values.                       |
| Duplicate removal   | None               | EDA. No duplicates found.                                 |
| Binary features     | Keep unchanged     | EDA: Binary features are already encoded and meaningful.                      |
| Numerical scaling   | **StandardScaler** | Good baseline for comparing multiple algorithms.     |
| Outlier removal     | None               | EDA. Preserve potentially informative defect samples.     |
| Feature selection   | None               | Evaluate feature importance after baseline training. |
| Feature engineering | None               | Keep the baseline simple and reproducible.           |

## Future Transformations

We are currently skipping these transformations:

- PCA
- Feature selection
- SMOTE
- Outlier removal
- Feature engineering

After the initial baseline we are going to evaluate possible integration of these transformations in the preprocessing pipeline. 


## Design Decisions

Use Scikit-Learn Pipelines.

- Reusable.
- Serializable.
- Easy to test.
- Industry standard.

Use Scikit-Learn ColumnTransformer to separate numerical columns from bianry columns.


## Open Questions
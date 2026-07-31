
PARAM_DISTRIBUTIONS_RF = dict(
        n_estimators=[100, 200, 300, 500],
        max_depth=[None, 10, 20, 30],
        min_samples_split=[2, 3, 4, 5, 6, 7],
        max_features=["sqrt", "log2"], 
    )


PARAM_DISTRIBUTIONS_XG = dict(
        n_estimators=[100, 200, 300, 500],
        learning_rate=[0.01, 0.03, 0.06, 0.1, 0.2, 0.3, 0.4],
        max_depth=[4, 7, 10, 13],
        subsample=[0.5, 0.7, 1.0],
        colsample_bytree=[0.7, 0.8, 1.0], 
    )


## Table of Contents

- [Project Purpose](#project-purpose)
- [Business Problem](#business-problem)
- [Goal](#goal)
- [Project Status](#project-status)
- [Quick Start](#quick-start)
- [Dataset](#dataset)
- [Software Requirements Specification](#software-requirements-specification-srs)
- [Architecture and  Repository Structure](#architecture-and-repository-structure)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Preprocessing](#preprocessing)
- [Baseline Model](#baseline-model)
- [Experiment Tracking](#experiment-tracking)
- [Project Roadmap](#project-roadmap)


## Project Purpose

This repository demonstrates software engineering and machine learning best practices for developing a production-oriented steel defect classification system.

The project follows an incremental development approach, including software requirements, architecture, testing, experiment tracking, and deployment, with each feature documented through GitHub Issues and Pull Requests.


## Business Problem

Predict the defect category of a manufactured steel plate using production measurements.

## Goal

 Develop a production-ready ML classification API capable of predicting one of seven defect categories.

![High-Level Architecture](docs/diagrams/High-Level-Architecture.jpg)


## Project Status

### Completed

- [x] Software Requirements Specification (SRS)
- [x] Repository structure
- [x] Exploratory Data Analysis
- [x] Preprocessing pipeline
- [x] Unit tests
- [x] Baseline Logistic Regression model
- [x] Model evaluation
- [x] Random Forest baseline
- [x] XGBoost baseline
- [x] Model comparison
- [x] MLflow experiment tracking

### Current Release

**Version:** v0.2.0


**Releaase name** Multiple Baseline Models and Model Evaluation

This release expands the machine learning pipeline to support multiple baseline algorithms, including Logistic Regression, Random Forest, and XGBoost. It introduces a generalized model factory, comparative model evaluation, MLflow experiment tracking across multiple models, and comprehensive reporting to support model selection prior to hyperparameter optimization.
## Quick Start

Clone the repository

```bash
git clone ...
```

Create environment 

```bash
python -m venev .venv
```
Activate
```
...
```
Install
```
pip install -r requirements.txt
```

Train a model

Select the desired model in:

```python
training/config.py

MODEL_NAME = RANDOM_FOREST
```

Available options:

- LOGISTIC_REGRESSION
- RANDOM_FOREST
- XGBOOST

Then run:

```bash
python -m training.train
```
Launch MLflow
```
mlflow ui
```


## Dataset


This project uses the **Steel Plates Faults** dataset from the UCI Machine Learning Repository.

The dataset description, feature definitions, and exploratory analysis can be found in:

- [`data/README.md`](data/README.md)

## Software Requirements Specification (SRS)

Initial requirements definition with the following list of sections can be found in  [`docs/SRS.md`](docs/SRS.md)

- Business Problem
- Business value

- API Consumer
- System overview
- Stakeholders
- Functional requirenments
- Open Questions

- In Scope (Version 1)
- Out of Scope (Version 1)
- Non-Functional requirements
- Assumptions
- Constraints


## Architecture and Repository Structure

The project follows a modular architecture separating:

- Data loading
- Preprocessing
- Model training
- Evaluation
- Inference

A Architecture and repository are vailable in: [`docs/Architecture.md`](docs/Architecture.md)

Design decisions (ADRs), Risk register, and diagrams are available in:

- [`docs/adr`](docs/adr)
- [`docs/Risk_Register`](docs/Risk_Register.md)
- [`docs/diagrams`](docs/diagrams)



## Exploratory Data Analysis

The dataset has been analyzed to understand:

- Class distribution
- Missing values
- Feature distributions
- Outliers
- Feature correlations

Main findings:

- No missing values
- Imbalanced target classes
- Numerical features with different scales
- Several outliers retained for the baseline model

Full EDA report can be found in: [`docs/Eda_Report.md`](docs/Eda_Report.md)

## Preprocessing

Current preprocessing pipeline:

- StandardScaler for numerical features
- Binary features passed through unchanged
- Scikit-learn ColumnTransformer
- Unit tested with pytest

Full preprocessing documentatioon can be found in [`docs/Preprocessing.md`](docs/Preprocessing.md)

## Baseline Model

- Stratified train/test split
- StandardScaler preprocessing
- Models evaluated:
  - Logistic Regression
  - Random forest
  - XGBoost
- Evaluation metrics:
  - Accuracy
  - Precision
  - Recall
  - Macro F1
- Classification report
- Confusion matrix

Full baseline model documentation can be found in [`docs/baseline_model_design.md`](docs/baseline_model_design.md) 

For detailed evaluation reports, confusion matrices, and model analysis, see:

- [`docs/logistic_regression_report.md`](docs/Logistic_regression_report.md)
- [`docs/random_forest_report.md`](docs/Random_forest_report.md)
- [`docs/xgboost_report.md`](docs/xgboost_report.md)

### Current Results 

| model | accuracy |      precision macro  |  recall macro | f1-score macro |f1-score weighted|  note|
|--------|--------|-----------|---------|----------|---|-----|
|logistic regression  | 0.72  |    0.76  |    0.73   |   0.74   | 0.72 |  baseline|
|random forest  | 0.80  |   **0.85**   |   0.79   |   **0.82**   | 0.80 |    candidate|
|XGBoost    |  **0.81**   |  0.82   |   **0.81**   |  0.81  |  **0.81** | candidate |

#### Current candidate models:
- random forest
- XGBoost
### Conclusion 
Random Forest and XGBoost significantly outperform the initial Logistic Regression baseline. While Random Forest achieved the highest Macro F1-score (0.82), XGBoost obtained the highest overall accuracy (0.81), weighted F1-score (0.81), and macro recall (0.81). Given the small performance difference, both models have been selected as candidate models for the hyperparameter optimization stage.

The result documentation can be found in [`docs/comparison_models.md`](docs/comparison_models.md)

## Experiment Tracking

Experiments are tracked using MLflow.

Each training run records:

- Training parameters
- Evaluation metrics
- Confusion matrix
- Trained model
- Preprocessor


## Project Roadmap


### v0.3.0
- Hyperparameter tuning
- Model selection

### v0.4.0
- FastAPI inference API

### v0.5.0
- Docker deployment

### v0.6.0
- GitHub Actions CI/CD

### v1.0.0
- Production-ready steel defect classification service
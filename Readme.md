

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
- [Model Development & Selection](#model-development-&-selection)
- [Experiment Tracking](#experiment-tracking)
- [Project Roadmap](#project-roadmap)
- [Release History](#release-history)


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
- [x] Random Forest baseline
- [x] XGBoost baseline
- [x] Model comparison and evaluation
- [x] MLflow experiment tracking
- [x] XGBoost hyperparameter refinement
- [x] Build and persist final model artifacts
- [x] MLflow final model tracking
- [x] Artifact and inference sanity tests
- [x] FastAPI inference service
- [x] `/health` endpoint
- [x] `/predict` endpoint
- [x] Pydantic request and response validation
- [x] API key authentication
- [x] Centralized model artifact loading with FastAPI lifespan
- [x] Controlled inference error handling
- [x] Request ID middleware
- [x] Application logging
- [x] API and logging tests

### Current Release

**Version:** v0.4.0  
**Release name:** FastAPI Inference API

This release exposes the selected XGBoost model through a FastAPI
inference service.

The API provides a public `/health` endpoint and a protected `/predict`
endpoint for steel defect classification. Prediction requests are
validated using Pydantic schemas and require an API key through the
`X-API-Key` HTTP header.

The trained model, preprocessing pipeline, label encoder, and model
metadata are loaded once during application startup using FastAPI's
lifespan mechanism.

The service also includes controlled inference error handling,
request-level identifiers for traceability, and application logging for
successful and failed prediction requests.

Automated tests cover prediction behavior, request validation,
authentication, error handling, request IDs, and logging.

The next milestone focuses on containerizing the inference service using
Docker.

## Quick Start

### Clone the repository

```bash
git clone <https://github.com/CarlosLara25/steel-defect-api.git>
cd steel-defect-api
```

### Create environment 

```bash
python -m venv .venv
```
Activate the environment
```
...
```
Install
```
pip install -r requirements.txt
```

### Configure environment variables

#### Create a local .env file based on .env.example.

Example:
```
API_KEY=your-api-key
```

* The .env file should not be committed to Git.

### Run the test suite
```
pytest
```

### Run the FastAPI application
```
python -m uvicorn app.main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

#### Health check
GET /health

#### Prediction

POST /predict

X-API-Key: your-api-key

* The request body must contain the 27 model input features.

### Train baseline models

#### Select the desired model in:

training/config.py

MODEL_NAME = RANDOM_FOREST

Available options:

LOGISTIC_REGRESSION
RANDOM_FOREST
XGBOOST

Then run:

python -m training.train

#### Train the selected model

python -m training.train_selected_model
Launch MLflow
mlflow ui

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

## Model Development & Selection

The project evaluates multiple machine learning models using a stratified
train/test split and a preprocessing pipeline based on `StandardScaler`.

### Models evaluated

- Logistic Regression
- Random Forest
- XGBoost

### Model selection process

The initial baseline experiment was followed by hyperparameter tuning of
the Random Forest and XGBoost candidate models.

The primary model selection metric is **Macro F1-score**, with stratified
5-fold cross-validation used during hyperparameter optimization.

Two XGBoost tuning experiments were performed. The second experiment
focused the search on promising regions identified during the first
experiment.

Further manual refinement was stopped because the second experiment did
not improve held-out test performance and did not provide sufficient
evidence for another focused search.

### Selected model

**XGBoost**

Selected configuration:

| Hyperparameter | Value |
|---|---:|
| n_estimators | 700 |
| learning_rate | 0.03 |
| max_depth | 9 |
| subsample | 0.6 |
| colsample_bytree | 0.9 |

### Final candidate performance

| Metric | Value |
|---|---:|
| Cross-validated Macro F1 | 0.8268 |
| Held-out Test Macro F1 | 0.8227 |

The selected model, preprocessing pipeline, label encoder, and metadata
are persisted as model artifacts and validated through automated sanity
tests.

Detailed documentation:

- [`docs/baseline_model_design.md`](docs/baseline_model_design.md)
- [`docs/hyperparameter_tuning_strategy.md`](docs/Hyperparameter_tuning_strategy.md)
- [`docs/hyperparameter_tuning_report.md`](docs/Hyperparameter_tuning_report.md)


## Experiment Tracking

Experiments are tracked using MLflow.

MLflow was used throughout model development to track:

- Model configurations
- Hyperparameters
- Cross-validation metrics
- Model selection experiments
- Training artifacts
- Final model training

Hyperparameter tuning experiments record individual candidate
configurations and their cross-validation results.

The final selected model training is also tracked as a separate MLflow run,
including the selected hyperparameters and persisted model artifacts.


## Project Roadmap


### v0.5.0
- Docker deployment

### v0.6.0
- GitHub Actions CI/CD

### v1.0.0
- Production-ready steel defect classification service

## Release History

**Version:** v0.1.0 \
**Releaase name** Baseline model

**Version:** v0.2.0 \
**Releaase name** Multiple Baseline Models and Model Evaluation

**Version:** v0.3.0  \
**Release name:** Model Selection & Final Training

**Version:** v0.4.0 \
**Release name:** Inference API


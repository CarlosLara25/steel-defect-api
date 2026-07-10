# Software Requirements Specification (SRS)

## Introduction

## Business Context

### Business Problem

Manufacturing processes may produce steel plates with different types of defects. Detecting these defects as early as possible helps reduce waste, improve product quality, and prevent defective products from reaching subsequent production stages. The objective of this project is to provide an ML-based prediction service capable of classifying steel plate defects using tabular process measurements.

### Business value

- Reduce defective products reaching later manufacturing stages.
- Support faster quality-control decisions.
- Provide consistent defect classification.
- Enable integration with manufacturing software (MES).
- Serve as a foundation for future AI-assisted inspection systems.

### API Consumer

- **Manufacturing Execution System (MES)** -> Requests Predictions during production and uses them within the manufacturing workflow

- **Internal Quality Control Software** -> Request predictions to support quelity engineers during inspection and analysis

### System overview

Factory Sensors\
&emsp;&emsp;&emsp;│\
        &emsp;&emsp;&emsp;▼\
Manufacturing Execution System (MES)\
        &emsp;&emsp;&emsp;│\
        &emsp;&emsp;&emsp;▼\
Steel Defect Detection API\
        &emsp;&emsp;&emsp;│\
        &emsp;&emsp;&emsp;▼\
Prediction Result\
        &emsp;&emsp;&emsp;│\
        &emsp;&emsp;&emsp;▼\
Quality Control Workflow

### Stakeholders

- **Production Engineer** Uses prediction results to monitor manufacturing quality.
- **Quality Engineer** Reviews uncertain or unexpected predictions.
- **Ml Engineer** Maintains and retrains the model.
- **Software Engineer** Maintains the API and deployment pipeline.
- **System Adminitrator** Maintains the production infrastructure.


## Functional requirenments
- **FR-001** The system shall accept a single steel plate sample for prediction.
- **FR-002** The system shall classify the sample into one of the seven defect categories.
- **FR-003**  The system shall return the prediction confidence.
- **FR-004**  The system shall include a prediction timestamp in every response.
- **FR-005**  The system shall include the model version in every response. 
- **FR-006**  The system shall recive all input features required by the deployed model.
- **FR-007**  The system shall generate a unique request for every request.
- **FR-008**  The system shall validate the structure, data types, and required fields of every incoming request.
- **FR-009**  The system shall return appropriate HTTP status codes for invalid requests or authentication failures.
- **FR-010**  The system require a valid API key before processing prediction requests.
- **FR-011**  The system shall log prediction requests and responses for auditing and troubleshooting purposes.
- **FR-012** The system shall expose a health endpoint indicating whether the prediction service is available.
- **FR-013**  The system shall load the deployed model during application startup and reuse it for subsequent predictions.
- **FR-014** The system shall return informative error messages when requests cannot be processed.

## Open Questions

- **OQ-001**  Should the ML API determine the operational decision
(accept/reject/manual inspection), or should this responsibility belong to the MES?
    
    **Status:**
Deferred to the architecture review.

---
### In Scope (Version 1)

- Single prediction endpoint
- Tabular data only
- Seven defect classes
- API key authentication
- MLflow experiment tracking
- Model version included in the response
- Docker deployment
- GitHub Actions CI
- Logging
- Unit and integration tests



### Out of Scope (Version 1)


- Image-based defect detection
- Batch prediction
- Automatic model retraining
- Cloud deployment
- User management (JWT)
- Database persistence
- Real-time monitoring dashboards
- Multiple deployed models

## Non-Functional requirements

- **NFR-001** The system shall return a prediction within 500 ms after the model has been loaded into memory
- **NFR-002** The application shall support at least one current prediction request.
- **NFR-003** The application shall continue serving prediction requests after invalid input requests.
- **NFR-004** The deployed model shall achieve a macro F1-score of at least 0.90 on the validation dataset.
- **NFR-005** Source code shall follow PEP 8 conventions.
- **NFR-006** The application shall include automated unit tests.
- **NFR-007** All code changes shall be version controlled using Git.
- **NFR-008** Prediction endpoints shall require API key authentication.
- **NFR-009** Sensitive configuration shall be stored in environment variables.
- **NFR-010** The application shall be deployable using Docker.
- **NFR-011** The application shall log prediction requests and unexpected errors.
- **NFR-012** Every prediction shall include the model version used.
- **NFR-013** The API shal provide automatically generated OpenAPI documentation.
- **NFR-014** Every commit to the repository shall trigger automated tests.

## Assumptions

- **A-001** Input data follows the schema used during model training.
- **A-002** Sensor measurements are already available before the AP is called.
- **A-003** Only one prediction is requested per API call in Version 1.
- **A-004** The deployed model has already been trained and validated.

## Constraints

- **C-001** Version 1 shall support only tabular data.
- **C-002** The initial implementation shall use scikit-learn
- **C-003** The project shall use Python 3.x.
- **C-004** The initial deployment target is a local Docker environment.
- **C-005** Authentication shall initially be implemented using API keys.

## High-Level Architecture

                   Client
             (MES / QC Software)
                       │
                       ▼
               FastAPI Application
                       │
      ┌────────────────┼────────────────┐
      │                │                │
      ▼                ▼                ▼
 Authentication  &emsp;&emsp; Request Validation &emsp;&emsp;&emsp;  Logging \
     &emsp;&emsp; │ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|    

      └────────────┬───┘
                   ▼
         Prediction Service
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
   Preprocessing     &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;    ML Model \
&emsp;&emsp;        │    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                 │       
&emsp;&emsp;└──────────┬───────┘\
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  ▼ \
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;            Prediction Response

## Architecture decisions records (ADRs)

- **ADR-001** 
    
    *Title:*  Use FastAPI as the API framework.
    
    *Context:* The system requires request validation, automatic documentation, and high performance.

    *Alternatives:* 
    - Flask 
    - Django REST Framework

    *Consequences:*
    - Automatic OpenAPI documentation
    - Native PYdantic integration
    - Async support
    - Learning curve for deendency injection

- **ADR-002**

    *Title:* Use scikit-learn for Version 1.

    *Alternatives:* 
    - XGBoost 
    - LightGBM
    - TensorFlow

    *Reason:* The project uses tabular data, focuses on software engineering practices, and scikit-learn provides a mature and simple API for classical ML models.

- **ADR-003**

    *Title:* Use Docker.

    *Context:* The application requires a reproducible execution environment that behaves consistently across development, testing, and deployment.

    *Alternatives:* 
    - Local python execution
    - Virtual machine deployment

    *Rationale:*  
    - Reproducible environments
    - Dependency isolation
    - Simplified onboarding
    - Consistent deployment
    - Easy integration with CI/CD
    - Cloud portability

- **ADR-004**

    *Title:* Authentication with API Key.

    *Alternatives:* 
    - JWT
    - OAuth2

    *Reason:*  Simpler implementation for an internal manufacturing API

- **ADR-005**

    *Title:* Experiment tracking with MLflow.

    *Context:* Multiple model experiments will be performed during development, and experiment reproducibility is required.

    *Alternatives:* 
    - TensorBoard
    - Weights & Biases
    - Manual experiments logs

    *Rationale:*
    - Track parameters and metrics automatically.
    - Store trained models as artifacts.
    - Improve experiment reproducibility.
    - Simplify comparison of model versions.
    - Prepare the project for future model registry and deployment workflows.


## Risk register

| ID    | Risk                      | Probability | Impact | Mitigation                                         |
| ----- | ------------------------- | ----------- | ------ | -------------------------------------------------- |
| R-001 | Model drift               | Medium      | High   | Retrain and monitor performance                    |
| R-002 | Invalid input values      | High        | Medium | Validate with Pydantic                             |
| R-003 | API unavailable           | Low         | High   | Docker restart policy and health endpoint          |
| R-004 | API key compromise        | Low         | High   | Rotate keys and store them securely                |
| R-005 | Low prediction confidence | Medium      | Medium | Return confidence score and allow client to decide |


## Requirements Traceability Matrix (RTM)

| ID    | Risk                      | Probability | Impact | Mitigation                                         |
| ----- | ------------------------- | ----------- | ------ | -------------------------------------------------- |


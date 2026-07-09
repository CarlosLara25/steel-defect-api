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
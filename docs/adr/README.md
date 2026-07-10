
## Architecture decisions records (ADRs)

- **ADR-001** 
    
    *Title:*  Use FastAPI as the API framework.
    
    *Context:* The system requires request validation, automatic documentation, and high performance.

    
- **ADR-002**

    *Title:* Use scikit-learn for Version 1.

    *Context:* The project uses tabular data, focuses on software engineering practices, and scikit-learn provides a mature and simple API for classical ML models.

- **ADR-003**

    *Title:* Use Docker.

    *Context:* The application requires a reproducible execution environment that behaves consistently across development, testing, and deployment.

- **ADR-004**

    *Title:* Experiment tracking with MLflow.

    *Context:* Multiple model experiments will be performed during development, and experiment reproducibility is required.

- **ADR-005**

    *Title:* Authentication with API Key.

    *Context:*  For Version 1 a simple implementation is enough for an internal manufacturing API




## Risk register

| ID    | Risk                      | Probability | Impact | Mitigation | Status                                        |
| ----- | ------------------------- | ----------- | ------ | -------------------------------------------------- | ---|
| R-001 | Model drift               | Medium      | High   | Retrain and monitor performance    |    Open                |
| R-002 | Invalid input values      | High        | Medium | Validate with Pydantic                          |    Open    |
| R-003 | API unavailable           | Low         | High   | Docker restart policy and health endpoint |    Open           |
| R-004 | API key compromise        | Low         | High   | Rotate keys and store them securely     | Open           |
| R-005 | Low prediction confidence | Medium      | Medium | Return confidence score and allow client to decide | Open|

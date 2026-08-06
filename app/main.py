from fastapi import FastAPI

app = FastAPI(
    title="Steel Defect Classification API",
    version="0.4.0",
)

@app.get("/health")
def health():
    return {"status": "ok"}
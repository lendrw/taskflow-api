from fastapi import FastAPI

app = FastAPI(title="TaskFlow API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "TaskFlow API"}


@app.get("/health")
def health():
    return {"status": "ok"}

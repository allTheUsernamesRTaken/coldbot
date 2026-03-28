from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="ColdBot API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# Lambda handler
handler = Mangum(app)

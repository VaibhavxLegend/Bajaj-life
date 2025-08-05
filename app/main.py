from fastapi import FastAPI, HTTPException, Request
from app.qa_pipeline import process_qa
from app.models import QARequest, QAResponse
from app.database import init_db

app = FastAPI(title="Insurance Policy QA API")

@app.on_event("startup")
async def startup():
    await init_db()

@app.post("/qa", response_model=QAResponse)
async def qa_endpoint(request: QARequest):
    try:
        return await process_qa(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

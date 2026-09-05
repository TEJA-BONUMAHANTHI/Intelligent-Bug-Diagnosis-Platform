from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.bug_submission import router as bug_router

app = FastAPI(
    title="Intelligent Bug Diagnosis Platform",
    description="Backend API for bug submission and diagnosis",
    version="1.0.0"
)

# Allow frontend running on localhost:5500
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    bug_router,
    prefix="/api/bugs",
    tags=["Bug Submission"]
)


@app.get("/")
def root():
    return {
        "message": "Intelligent Bug Diagnosis Platform API is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
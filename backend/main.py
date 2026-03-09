from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from auth.router      import router as auth_router
from api.resume       import router as resume_router
from api.github       import router as github_router
from api.internships  import router as internships_router
from api.roadmap      import router as roadmap_router
from api.linkedin     import router as linkedin_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CareerAI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router,        prefix="/auth",        tags=["Authentication"])
app.include_router(resume_router,      prefix="/resume",      tags=["Resume Analyzer"])
app.include_router(github_router,      prefix="/github",      tags=["GitHub Analyzer"])
app.include_router(internships_router, prefix="/internships", tags=["Internship Finder"])
app.include_router(roadmap_router,     prefix="/roadmap",     tags=["AI Roadmap"])
app.include_router(linkedin_router,    prefix="/linkedin",    tags=["LinkedIn Analyzer"])

@app.get("/")
def root():
    return {"message": "CareerAI API is running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "ok"}
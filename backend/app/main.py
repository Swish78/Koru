from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Koru API", version="0.1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
from app.api.v1 import auth as auth_router

app.include_router(
    auth_router.router,
    prefix="/api/v1/auth",
    tags=["auth"]
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Koru API"}
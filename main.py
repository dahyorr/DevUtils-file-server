from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import files
from config import ORIGINS

app = FastAPI()
app.include_router(files.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_methods=["POST", "DELETE"],
    allow_headers=["*"],
)


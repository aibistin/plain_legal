from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import psa

app = FastAPI(title="Plain Legal API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(psa.router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}

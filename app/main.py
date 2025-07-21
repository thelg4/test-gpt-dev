from fastapi import FastAPI
from .api.routes import router

app = FastAPI(title="CSV Analyzer API")
app.include_router(router)
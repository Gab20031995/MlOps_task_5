from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uuid

from starlette import status

app = FastAPI(
    title="API's Task 5 MLops",
    version="0.0.1"
)

@app.post("/api/v1/register/")
async def create_user(username: str, name: str):
    return {
        "username": username,
        "email": name,
        "Password": str,
        "message": "The user has been created successfully",
        "status_Code": 201
    }
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette import status
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI(
    title="API's Task 5 MLops",
    version="0.0.1"
)

# Simulación de almacenamiento de datos en memoria
db_users = {}
db_tasks = {}

class User(BaseModel):
    username: str
    email: str
    password: str

class Task(BaseModel):
    title: str
    description: str
    status: str

#Registro de Usuarios:
@app.post("/api/v1/register/")
async def create_user(user: User):
    if user.username in db_users:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    db_users[user.username] = user
    return {
        "username": user.username,
        "email": user.email,
        "Password": user.password,
        "message": "The user has been created successfully",
        "status_Code": 201
    }

#Obtener Datos de Usuario:
@app.get("/api/v1/user/{username}")
async def get_user(username: str):
    if username in db_users:
        user = db_users[username]
        return user
    else:
        return JSONResponse(
            content={"message": "User not found"},
            status_code=status.HTTP_404_NOT_FOUND
        )


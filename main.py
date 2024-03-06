from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uuid

from starlette import status

#Registro de Usuarios:
app = FastAPI(
    title="API's Task 5 MLops",
    version="0.0.1"
)

@app.post("/api/v1/register/")
async def create_user(username: str, name: str,password: str):
    return {
        "username": username,
        "email": name,
        "Password": password,
        "message": "The user has been created successfully",
        "status_Code": 201
    }

#Obtener Datos de Usuario:

@app.get("/api/v1/user/{user_id}")
async def get_user(user_id: str):
    # Aquí iría la lógica para obtener los datos del usuario con el ID proporcionado
    # Por simplicidad, devolvemos un usuario de ejemplo si el ID es "1"
    if user_id == "1":
        return {
            "user_id": user_id,
            "username": "example_user",
            "email": "example@example.com"
        }
    else:
        return JSONResponse(
            content={"message": "User not found"},
            status_code=status.HTTP_404_NOT_FOUND
        )

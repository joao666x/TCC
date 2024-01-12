from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from api.serializers.response import ApiResponse
from api.utils.auth import get_current_user
from api.serializers.login import UserRetrieveSerializer

routers = APIRouter()

@routers.get("/", response_model=ApiResponse)
def hello_world():
    return {"message": "Hello World!"}

@routers.post("/say_my_name", response_model=ApiResponse)
def say_my_name(name: str = Body(embed=True)):
    return {"message": f"Olá {name}!"}

@routers.get("/whoami", response_model=UserRetrieveSerializer)
def whoami(current_user: UserRetrieveSerializer = Depends(get_current_user)):
    return jsonable_encoder(current_user)

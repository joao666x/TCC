# TODO: Esse endpoint se tornará uma CLI posteriormente
from fastapi import APIRouter

from api.serializers.response import ApiResponse
from api.utils.auth import get_password_hash
from api.database.models import User
from api.database.db_conn import get_session
from api.serializers.login import CreateUser

routers = APIRouter()

@routers.post("/create_user", response_model=ApiResponse)
def crete_user(user: CreateUser):
    new_user = User(
        name = user.name,
        email = user.email,
        password = get_password_hash(user.password)
    )
    with get_session().begin() as session:
        session.add(new_user)
    return {"message": "created"}

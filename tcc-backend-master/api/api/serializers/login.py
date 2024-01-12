from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class UserRetrieveSerializer(BaseModel):
    name: str
    email: str

class CreateUser(BaseModel):
    name: str
    email: str
    password: str
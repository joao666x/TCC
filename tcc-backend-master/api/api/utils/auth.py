from copy import deepcopy
from datetime import timedelta, datetime

from sqlalchemy import select
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from api.database.db_conn import get_session
from api.database.models import User

SECRET_KEY = "123"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(password_to_check, hashed_password):
    return pwd_context.verify(password_to_check, hashed_password)

def authenticate_user(email: str, password: str):
    with get_session().begin() as session:
        query = select(User)
        query = query.where(User.email == email)
        user = session.scalars(query).one_or_none()
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        current_user = deepcopy(user)
    return current_user

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=1)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    with get_session().begin() as session:
        query = select(User)
        query = query.where(User.id == user_id)
        user = session.scalars(query).one_or_none()
        current_user = deepcopy(user)
    if current_user is None:
        raise credentials_exception
    return current_user
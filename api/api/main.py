from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import example, login, create_user

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#include routers
app.include_router(example.routers)
app.include_router(login.routers)
# Esse router será excluido posteriormente para virar uma CLI
app.include_router(create_user.routers)
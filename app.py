from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.form import handler
from db.postgres.connection import db, connection, check_connection



app = FastAPI()
app.include_router(handler.router)

# only on development
check_connection();


origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



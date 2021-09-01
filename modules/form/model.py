from pydantic import BaseModel,ValidationError, validator
from typing import Any

from pydantic.networks import EmailStr

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

SQLALCHEMY_DATABASE_URL = "postgresql://postgres: @localhost/topskill"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Business(BaseModel):
    businessName: str
    fullName: str
    businessEmail:EmailStr
    role:str
    service: str
    teamSize: int

class Business(Base):
    __tablename__ = "business"

    id = Column(String, primary_key=True, index=True)
    businessName = Column(String,index=True)
    fullName=Column(String,index=True)
    businessEmail= Column(String,index=True)
    role= Column(String,index=True)
    service= Column(String,index=True)
    teamSize= Column(Integer,index=True)
    


class Skill_up_africa(BaseModel):
    full_name:str
    phone_number:int
    email:EmailStr
    country:str
    career_path:str
    experience:str
    referal:str
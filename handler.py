from pydantic import BaseModel,ValidationError, validator
from typing import Any

from pydantic.networks import EmailStr

class Business(BaseModel):
    businessName: str
    fullName: str
    businessEmail:EmailStr
    role:str
    service: str
    teamSize: int
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

class Skill_up_africa(BaseModel):
    full_name:str
    phone_number:int
    email:EmailStr
    country:str
    career_path:str
    experience:str
    referal:str
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)


class Login(BaseModel):
    email:EmailStr
    password:str
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

class SignUp(BaseModel):
    email:EmailStr
    full_name:str
    password:str
    confirm_password:str
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
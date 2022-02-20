# Python
from datetime import date
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    '''
    Model UserBase to simulate at Twitter's User, this not contain the password
    '''
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)
    
    class Config:
        schema_extra = {
            "example": {
                "user_id"       : '12346-a2ff4hgh-123040-2cds2x',
                "email"         : "danielcaamal@email.com",
                "first_name"    : "Daniel",
                "last_name"     : "Caamal",
            }
        }


class UserLogin(UserBase):
    '''
    Model User Login to simulate at Twitter's User, this inherit BaseUser and needs a password 
    to be completed,  this only must implemented for request bodies
    '''
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example='a1s2s3242ch5678'
    )

class User(UserBase):
    '''
    Model User to simulate at Twitter's User, this inherit BaseUser and returns all the fields 
    but not the password, this only must implemented for response bodies
    '''
    pass
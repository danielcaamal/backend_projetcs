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
                "user_id"       : "a8098c1a-f86e-11da-bd1a-00112444be1e",
                "email"         : "danielcaamal@email.com",
                "first_name"    : "Daniel",
                "last_name"     : "Caamal",
                "birth_date"     : date(2000,1,1)
            }
        }

class UserPasswordMixin():
    '''
    Model UserPasswordMixin allows to implement when to use password as request and avoid return it
    int the response
    '''
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example='a1s2s3242ch5678'
    )


class UserLogin(UserBase, UserPasswordMixin):
    '''
    Model User Login to simulate at Twitter's User, this inherit BaseUser and needs a password 
    to be completed,  this only must implemented for request bodies and only for login
    '''
    
class UserRegister(UserBase, UserPasswordMixin):
    '''
    Model User Register to simulate at Twitter's User, this inherit BaseUser and needs a password 
    to be completed,  this only must implemented for request bodies and only for register a User
    '''

class User(UserBase):
    '''
    Model User to simulate at Twitter's User, this inherit BaseUser and returns all the fields 
    but not the password, this only must implemented for response bodies
    '''
    pass
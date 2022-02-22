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
    user_id: int = Field(...)
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
                "user_id"       : 1,
                "email"         : "danielcaamal@email.com",
                "first_name"    : "Daniel",
                "last_name"     : "Caamal",
                "birth_date"     : date(2000,1,1)
            }
        }

class UserPasswordMixin(BaseModel):
    '''
    Model UserPasswordMixin allows to implement when to use password as request and avoid return it
    int the response
    '''
    user_id: Optional[int] = Field()
    first_name: Optional[str] = Field()
    last_name: Optional[str] = Field()
    email: EmailStr = Field(...) 
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example='a1s2s3242ch5678'
    )
    


class UserLogin(UserPasswordMixin):
    '''
    Model User Login to simulate at Twitter's User, this inherit BaseUser and needs a password 
    to be completed,  this only must implemented for request bodies and only for login
    '''
    email: EmailStr = Field(...)
    
    class Config:
        schema_extra = {
                "example": {
                    "email"         : "danielcaamal@email.com",
                    "password"      : "0123456789",
                }
            }
    
class UserRegister(UserBase, UserPasswordMixin):
    '''
    Model User Register to simulate at Twitter's User, this inherit BaseUser and needs a password 
    to be completed,  this only must implemented for request bodies and only for register a User
    '''
    class Config:
        schema_extra = {
            "example": {
                "user_id"       : 1,
                "email"         : "danielcaamal@email.com",
                "password"      : "0123456789",
                "first_name"    : "Daniel",
                "last_name"     : "Caamal",
                "birth_date"     : date(2000,1,1)
            }
        }

class User(UserBase):
    '''
    Model User to simulate at Twitter's User, this inherit BaseUser and returns all the fields 
    but not the password, this only must implemented for response bodies
    '''
    def from_dict(obj):
        '''Serializer for Model User'''
        user = {}
        user['user_id'] = obj['id']
        user['first_name'] = obj['first_name']
        user['last_name'] = obj['last_name']
        user['email'] = obj['email']
        user['birth_date'] = (obj['birth_date']).strftime('%Y-%m-%d')
        return user
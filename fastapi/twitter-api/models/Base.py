# Python

# Pydantic
from pydantic import BaseModel, EmailStr, Field

class BaseResponse():
    '''
    Model Base to add in the response models
    '''
    status: int = Field(
        ..., 
        example=1
    )
    message: str = Field(
        ...,
        example='Response successfully'
    )
# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# Fast API
from fastapi import FastAPI, Query, Path
from fastapi import Body
from fastapi.logger import logger

app = FastAPI(debug=True)

@app.get('/')
def home():
    logger.info('HELLO WORLD')
    return {'hello': 'world'}


# Models
class HairColor(Enum):
    white =     'white'
    brown =     'brown'
    black =     'black'
    blonde =    'blonde'


class Person(BaseModel):
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
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        example='black'
    )
    is_married: Optional[bool] = Field(
        default=None
    )
    
    class Config:
        schema_extra = {
            "example": {
                "first_name"    : "Daniel",
                "last_name"     : "Caamal",
                "age"           : 25,
                "hair_color"    : "black",
                "is_married"    : False
            }
        }


class Location(BaseModel):
    city: str
    state: str
    country: str
    
    class Config:
        schema_extra = {
            "example": {
                "city"      : "Mexico",
                "state"     : "Mexico",
                "country"   : "Mexico"
            }
        }

# Query Parameters /person/detail?name=name&age=age
# The Query parameters are optional, is a bad practice use them as obligatory
@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
            None, min_length=1, 
            max_length=50,
            title='Person Name',
            description='This is the person name'
        ),
    age: Optional[int] = Query(
            ..., 
            description='Person Age, it is required'
        )
):
    return {name:age}


# Path parameters /person/detail
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(..., gt=0, example=1, description='Person id, greater than 0')
):
    return { person_id: 'It exists' }


# Request body
@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person

@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(
        ...,
        title='Person ID',
        description='This is the person ID',
        gt=0
    ),
    person: Person = Body(
        ...
    ),
    location: Location = Body(
        ...
    )
):
    result = person.dict()
    result.update(location.dict())
    return result
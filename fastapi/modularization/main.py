# Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# Fast API
from fastapi import Body, Cookie, FastAPI, File, Form, Header, HTTPException, Path, Query, status, UploadFile
from fastapi.logger import logger

app = FastAPI(debug=True)

@app.get(
    '/', 
    status_code=status.HTTP_200_OK
)
def home():
    logger.info('HELLO WORLD')
    return {'hello': 'world'}

# Models
class HairColor(Enum):
    white =     'white'
    brown =     'brown'
    black =     'black'
    blonde =    'blonde'

class PersonBase(BaseModel):
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

class Person(PersonBase):
    password: str = Field(
        ...,
        min_length=8
    )
    class Config:
        schema_extra = {
            "example": {
                "first_name"    : "Daniel",
                "last_name"     : "Caamal",
                "age"           : 25,
                "hair_color"    : "black",
                "is_married"    : False,
                "password"      : "Daniel"
            }
        }

# Response Model
class PersonOut(PersonBase):
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

class LoginOut(BaseModel):
    username: str  = Field(
        ..., 
        max_length=20,
        example='Daniel01'
    )
    message: str = Field(
        default='Login Successfully'
    )

# Query Parameters /person/detail?name=name&age=age
# The Query parameters are optional, is a bad practice use them as obligatory
@app.get(
    '/person/detail',
    status_code=status.HTTP_200_OK,
    tags=['Persons'],
    deprecated=True
)
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


persons = [1,2,3,4,5]

# Path parameters /person/detail
@app.get(
    '/person/detail/{person_id}', 
    status_code=status.HTTP_200_OK,
    tags=['Persons']
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0, 
        example=1, 
        description='Person id, greater than 0'
    )
):
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                'status': 0,
                'message': 'This person doesn\'t exist'
            }
        )
    return { person_id: 'It exists' }

# Request body
@app.post(
    '/person/new',
    response_model=PersonOut, 
    status_code=status.HTTP_201_CREATED,
    response_description='Person created',
    tags=['Persons'],
    summary='Create Person in the app',
)
def create_person(person: Person = Body(...)):
    '''
    Create Person
    
    This path operation creates a Person in the app and save the information in the database.
    
    Parameters:
    - Request body parameter:
        - **person: Person** -> A Person model with first name, last name, age, hair color and marital status
    
    Returns a Person model with first name, last name, age, hair color and marital status
    
    '''
    return person

@app.put(
    '/person/{person_id}', 
    status_code=status.HTTP_200_OK,
    response_description='Person updated',
    tags=['Persons']
)
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

# Forms
@app.post(
    path='/login',
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
)
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return LoginOut(username=username)

# Cookies and Headers Parameters
@app.post(
    path='/contact',
    status_code=status.HTTP_200_OK
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1,
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1,
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent

# Files
@app.post(
    path='/post-image',
)
def post_image(
    image: UploadFile = File(...)
):
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024,ndigits=2),
    }

# Handling Errors
# @app.post(
    
# )


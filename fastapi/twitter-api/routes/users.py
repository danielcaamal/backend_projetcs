# Python
import simplejson as json

# FastAPI
from typing import List
from fastapi import APIRouter, Body, status, HTTPException, Path

# My imports
from models.User import *


router = APIRouter()

## Path Operations - User

### Create a User
@router.post(
    path='/signup',
    response_model=UserRegister,
    status_code=status.HTTP_201_CREATED,
    summary='Register a User',
    tags=['Users']
)
def signup(
    user: UserRegister = Body(...)
):
    '''
    Signup
    
    This path operation register a new user in the app
    
    Parameters:
        - Request body parameter
            - user: UserRegister
            
    Returns a json with basic information (Model User):
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    '''
    with open('users.json', 'r+', encoding='utf-8') as file:
        users = json.loads(file.read())
        new_user = user.dict()
        
        # Serialization
        new_user['user_id'] = str(new_user['user_id'])        
        new_user['birth_date'] = str(new_user['birth_date'])
        
        # Validations
        if new_user['user_id'] in [ key['user_id'] for key in users ]:
            raise HTTPException(status.HTTP_409_CONFLICT,detail={'msg': 'user already exists'})
        
        users.append(new_user)
        file.seek(0)
        file.write(json.dumps(users))
        return new_user

### Login User
@router.post(
    path='/login',
    response_model=UserLogin,
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=['Users']
)
def login():
    pass

### Show all Users
@router.get(
    path='/',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all Users',
    tags=['Users']
)
def show_all_users():
    '''
    Show all users
    
    This path operation show all users in the application
    
    Parameters:
        - 
    
    Returns a json with basic information (Users List[User]):
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    '''
    with open('users.json', 'r', encoding='utf-8') as file:
        users = json.loads(file.read())
        return users

### Show Users
@router.get(
    path='/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show User',
    tags=['Users']
)
def show_user(
    user_id: str = Path(...)
):
    '''
    Show user by user_id
    
    This path operation show the user if it exists
    
    Parameters:
        - user_id: UUID
    
    Returns a json with basic information (User):
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    
    If not exist returns:
        - message: str
    '''
    with open('users.json', 'r', encoding='utf-8') as file:
        users = json.loads(file.read())
        for user in users:
            if user['user_id'] == user_id:
                return user
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={'msg': 'This user doesn\'t exists'})

# Update User
@router.put(
    path='/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update User',
    tags=['Users']
)
def update_user(
    user_id: str = Path(...),
    user: User = Body(...)
):
    '''
    Update user by user_id
    
    This path operation update the user if it exists
    
    Parameters:
        - user_id: UUID
    
    Returns a json with basic information (User):
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    
    If not exist returns:
        - message: str
    '''
    with open('users.json', 'r+', encoding='utf-8') as file:
        users = json.loads(file.read())
        updated_user = user.dict()
        for u in users:
            if u['user_id'] == user_id:
                u = updated_user
                file.seek(0)
                file.write(json.dumps(users))
                return updated_user
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={'msg': 'This user doesn\'t exists'})

# Delete User
@router.delete(
    path='/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete User',
    tags=['Users']
)
def delete_user():
    pass


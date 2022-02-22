# Python
from datetime import datetime, date
import simplejson as json
from dateutil.parser import parse

# FastAPI
from typing import List
from fastapi import APIRouter, Body, status, HTTPException, Path
from database.Connection import PoolCursor

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
        - user_id: int
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: Optional[date]
    '''
    with PoolCursor() as cursor:
        new_user = user.dict()
        query = "SELECT * FROM users WHERE id = {user_id} OR email = '{email}';".format(**new_user)
        cursor.execute(query)
        # If the cursor returns something then we raise an error (user repeated)
        if cursor.rowcount > 0:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'msg':'User already exists'})
        
        if not new_user.get('birth_date', False): new_user['birth_date'] = None
            
        query = """
            INSERT INTO users (email, password, first_name, last_name, birth_date) 
            VALUES ('{email}', '{password}', '{first_name}', '{last_name}', '{birth_date}');
        """.format(**new_user)
        cursor.execute(query)
        
        if cursor.rowcount > 0:
            return new_user
        
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail={'msg':'Something wrong happened'})
        

### Login User
@router.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a User',
    tags=['Users']
)
def login(
    user: UserLogin = Body(...)
):
    with PoolCursor() as cursor:
        login_user = user.dict()
        
        # Execute
        query = "SELECT * FROM users WHERE password = '{password}';".format(**login_user)
        cursor.execute(query)
        
        # If the cursor returns something then we raise an error (user repeated)
        if cursor.rowcount <= 0:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'msg':'User not register with this password'})
        
        # Serialize result
        logged_user = User.from_dict(cursor.fetchone())
        return logged_user


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
    with PoolCursor() as cursor:
        
        # Execute
        query = "SELECT * FROM users"
        cursor.execute(query)
        
        users = []
        # Serialize result
        for user in cursor.fetchall():
            users.append(User.from_dict(user))
        
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
    with PoolCursor() as cursor:
        
        # Execute
        query = "SELECT * FROM users WHERE id = '{}';".format(user_id)
        cursor.execute(query)
        
        # If the cursor returns something then we raise an error (user repeated)
        if cursor.rowcount <= 0:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'msg':'User not register with this password'})
        
        # Serialize result
        return User.from_dict(cursor.fetchone())

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
    with PoolCursor() as cursor:
        update_user = user.dict()
        # Execute
        query = "SELECT * FROM users WHERE id = '{}';".format(user_id)
        cursor.execute(query)
        
        # If the cursor returns something then we raise an error (user repeated)
        if cursor.rowcount <= 0:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'msg':'User not exists'})
        
        query = """
            UPDATE users 
            SET email='{email}', first_name='{first_name}', last_name='{last_name}', birth_date='{birth_date}' 
            WHERE id = {user_id}
        """.format(**update_user)
        cursor.execute(query)
        
        if cursor.rowcount > 0:
            return update_user
        
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail={'msg':'Something wrong happened'})

# Delete User
@router.delete(
    path='/{user_id}',
    status_code=status.HTTP_200_OK,
    summary='Delete User',
    tags=['Users']
)
def delete_user(
    user_id: str = Path(...),
):
    with PoolCursor() as cursor:
        # Execute
        query = "SELECT * FROM users WHERE id = '{}';".format(user_id)
        cursor.execute(query)
        
        # If the cursor returns something then we raise an error (user repeated)
        if cursor.rowcount <= 0:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'msg':'User not exists'})
        
        query = "DELETE FROM users WHERE id = '{}';".format(user_id)
        cursor.execute(query)
        
        if cursor.rowcount > 0:
            return {'msg':'Delete successfully'}
        
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail={'msg':'Something wrong happened'})


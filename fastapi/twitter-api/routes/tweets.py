# Python
import simplejson as json

# FastAPI
from typing import List
from fastapi import APIRouter, Body, status, HTTPException, Path

# My imports
from models.Tweet import *


router = APIRouter()

##  Path Operations - Tweets

### Show all Tweets
@router.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all Tweets',
    tags=['Tweets']
)
def home():
    '''
    Show all tweets
    
    This path operation show all tweet in the app.
    
    Parameters:
        - 
    
    Returns a json with basic information (List[Tweet]):
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - By: User
            - user_id: UUID
            - email: EmailStr
            - first_name: str
            - last_name: str
            - birth_date: date
    '''
    with open('tweets.json', 'r+', encoding='utf-8') as file:
        return json.loads(file.read())

### Create a Tweet
@router.post(
    path='/',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a Tweet',
    tags=['Tweets']
)
def post_tweet(
    tweet: Tweet = Body(...)
):
    '''
    Post tweet
    
    This path operation post a tweet in the application
    
    Parameters:
        - 
    
    Returns a json with basic information (Tweet):
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - By: User
            - user_id: UUID
            - email: EmailStr
            - first_name: str
            - last_name: str
            - birth_date: date
    '''
    with open('tweets.json', 'r+', encoding='utf-8') as file:
        tweets = json.loads(file.read())
        new_tweet = tweet.dict()
        
        # Serialization Tweet
        new_tweet['tweet_id'] = str(new_tweet['tweet_id'])       
        new_tweet['created_at'] = str(new_tweet['created_at'])
        if new_tweet.get('updated_at', False):
            new_tweet['updated_at'] = str(new_tweet['updated_at'])
        
        # Serialization User
        new_tweet['by']['user_id'] = str(new_tweet['by']['user_id'])
        new_tweet['by']['birth_date'] = str(new_tweet['by']['birth_date'])
        
        
        # Validations
        if new_tweet['tweet_id'] in [ key['tweet_id'] for key in tweets ]:
            raise HTTPException(status.HTTP_409_CONFLICT,detail={'msg': 'tweet not allowed'})
        
        tweets.append(new_tweet)
        file.seek(0)
        file.write(json.dumps(tweets))
        return new_tweet

### Show a Tweet
@router.get(
    path='/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a Tweet',
    tags=['Tweets']
)
def show_tweet():
    pass

### Delete a Tweet
@router.put(
    path='/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a Tweet',
    tags=['Tweets']
)
def delete_tweet():
    pass

### Delete a Tweet
@router.delete(
    path='/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a Tweet',
    tags=['Tweets']
)
def delete_tweet():
    pass
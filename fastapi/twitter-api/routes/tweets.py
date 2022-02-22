# Python
import simplejson as json

# FastAPI
from typing import List
from fastapi import APIRouter, Body, status, HTTPException, Path
from database.Connection import PoolCursor

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
    with PoolCursor() as cursor:
        
        # Execute
        query = "SELECT t.id as tweet_id,* FROM tweets t INNER JOIN users u ON u.id=t.user_id"
        cursor.execute(query)
        
        tweets = []
        # Serialize result
        for res in cursor.fetchall():
            user = User.from_dict(res)
            tweet = Tweet.from_dict(res)
            tweet['by'] = user
            tweets.append(tweet)
        print(tweets)
        return tweets


### Create a Tweet
@router.post(
    path='/',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a Tweet',
    tags=['Tweets']
)
def post_tweet(
    tweet: Tweet = Body(...),
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
    with PoolCursor() as cursor:
        try:
            new_tweet = tweet.dict()
            
            if not new_tweet.get('updated_at', False): new_tweet['updated_at'] = None
            
            user_id = new_tweet['by']['user_id']
            new_tweet['user_id'] = user_id
            query = """
                INSERT INTO tweets (id, content, created_at, updated_at, user_id) 
                VALUES ('{tweet_id}', '{content}', '{created_at}', '{updated_at}', '{user_id}');
            """.format(**new_tweet)
            cursor.execute(query)
            
            if cursor.rowcount > 0:
                query = "SELECT * FROM users WHERE id = '{}';".format(user_id)
                cursor.execute(query)
                new_tweet['by'] = User.from_dict(cursor.fetchone())
                print(new_tweet)
                return new_tweet
        
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'msg':f'{err}'})
        

### Show a Tweet
@router.get(
    path='/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a Tweet',
    tags=['Tweets']
)
def show_tweet(
    tweet_id: str = Path(...),
):
    # Execute
    with PoolCursor() as cursor:
        query = "SELECT u.id as user_id, t.id as tweet_id, * FROM tweets t INNER JOIN users u ON u.id=t.user_id WHERE t.id = '{}'".format(tweet_id)
        print(query)
        cursor.execute(query)
        
        tweets = []
        # Serialize result
        res = cursor.fetchone()
        print(res)
        user = User.from_dict(res)
        tweet = Tweet.from_dict(res)
        tweet['by'] = user
        print(tweet)
        return tweet

### Delete a Tweet
@router.put(
    path='/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a Tweet',
    tags=['Tweets']
)
def update_tweet(
    tweet_id: str = Path(...),
    tweet: Tweet = Body(...),
):
    with PoolCursor() as cursor:
        update_tweet = tweet.dict()
        # Execute
        query = "SELECT * FROM tweets WHERE id = '{}';".format(tweet_id)
        cursor.execute(query)
        
        # If the cursor returns something then we raise an error (user repeated)
        if cursor.rowcount <= 0:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'msg':'Tweet not exists'})
        
        update_tweet['user_id'] = update_tweet['by']['user_id']
        query = """
            UPDATE tweets 
            SET content='{content}', updated_at='{updated_at}', created_at='{created_at}', user_id='{user_id}' 
            WHERE id = {tweet_id}
        """.format(**update_tweet)
        cursor.execute(query)
        
        if cursor.rowcount > 0:
            return update_tweet
        
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail={'msg':'Something wrong happened'})

### Delete a Tweet
@router.delete(
    path='/{tweet_id}',
    status_code=status.HTTP_200_OK,
    summary='Delete a Tweet',
    tags=['Tweets']
)
def delete_tweet(
    tweet_id: str = Path(...),
):
    # Execute
    with PoolCursor() as cursor:
    
        query = "SELECT * FROM tweets WHERE id = '{}';".format(tweet_id)
        cursor.execute(query)
        
        # If the cursor returns something then we raise an error (user repeated)
        if cursor.rowcount <= 0:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'msg':'Tweet not exists'})
        
        query = "DELETE FROM tweets WHERE id = '{}';".format(tweet_id)
        cursor.execute(query)
        
        if cursor.rowcount > 0:
            return {'msg':'Delete successfully'}
        
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail={'msg':'Something wrong happened'})
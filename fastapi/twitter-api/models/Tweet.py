# Python
from datetime import datetime
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel, Field

# My imports
from models.User import User

class Tweet(BaseModel):
    '''Model Tweet to simulate at Twitter's basic tweet.'''
    tweet_id: int = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=255
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
    
    def from_dict(obj):
        tweet = {}
        tweet['tweet_id'] = obj['tweet_id']
        tweet['content'] = obj['content']
        tweet['created_at'] = obj['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        tweet['updated_at'] = obj['updated_at'].strftime('%Y-%m-%d %H:%M:%S') if obj.get('updated_at', False) else None
        tweet['by'] = obj['user_id']
        return tweet
        
        
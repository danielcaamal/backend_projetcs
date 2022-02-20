# Python
from datetime import datetime
from typing import Optional
from uuid import UUID

# Pydantic
from pydantic import BaseModel, Field

# My imports
from models.User import User

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=255
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)
    
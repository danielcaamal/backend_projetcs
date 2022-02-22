# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel, Field

class TimestampMixin(BaseModel):
    created_at: datetime = Field(
        default_factory = datetime.utcnow,
        description = 'The time the document was created.'
    )
    updated_at: datetime = Field(
        default=None,
        description='The time the document was last updated.'
    )
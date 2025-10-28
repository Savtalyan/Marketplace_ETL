from sqlmodel import SQLModel
from typing import Optional, Annotated, Field
from datetime import datetime
from pydantic import BeforeValidator
from typing_extensions import Annotated


# Reusable annotated types 
PrimaryKey = Annotated[int, Field(primary_key=True)]
Datetime = Annotated[datetime, Field(default_factory=datetime.now())]
StatusType = Annotated[str, Field(default="pending", description="status of the job")]
NameType = Annotated[str, Field(min_length=1, max_length=100, description="name: type")]

# Base model 
class BaseModel(SQLModel):
    """ Base model for reuse

    Args:
        SQLModel (_type_): _description_
    """
    id : Optional[PrimaryKey] = None
    created_at : Datetime
    updated_at : Datetime 
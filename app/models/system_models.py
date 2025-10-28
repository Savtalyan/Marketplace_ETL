from sqlmodel import Field
from typing import Optional, Annotated
from .base import BaseModel, Datetime


## system models 


class User(BaseModel, table=True):
    """ User model

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__="users"

    username : Annotated[str, Field(min_length=8, max_length=20)] # TODO implement validation rule for email and use here
    password_hash : Annotated[str, Field(description="password hash code")]
    is_active : bool = Field(default=True)
    last_login_at : Optional[Datetime] = None 



class APIToken(BaseModel, table=True):
    """ API token model

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__="api_tokens"

    user_id : Annotated[int, Field(foreign_key="users.id")]
    token : Annotated[str, Field(description="API token")]
    expires_at : Annotated[Datetime, Field(description="token expiration datetime")]
    last_used_at : Annotated[Datetime, Field(description="Last time the token has been used")]
    rate_limit_per_hour : Annotated[int, Field(description="Rate limit per hour for this token")]
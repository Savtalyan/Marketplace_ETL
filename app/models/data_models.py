from sqlmodel import Field
from typing import Optional, Annotated, Dict
from .base import BaseModel, NameType, Datetime


# Marketplace model

class Marketplace(BaseModel, table=True):
    """ Model for each marketplace 

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """

    __tablename__ = "marketplaces"

    name : Annotated[str, Field(description="Marketplace to be scraped", min_length=2, max_length=100)]
    code : Annotated[str, Field(description="Code of the marketplace")]
    base_url : Annotated[str, Field(description="Marketplace base url")]
    is_active : Optional[bool] = None
    rate_limit_per_minute : Optional[int] = None
    requires_authentication : Annotated[bool, Field(description="Marketplace authentication necessity")]

    # TODO implement relationship, and enum selection of scraper
    default_scraper : Annotated[str, Field(description="scraper for specific marketplace")]



class ScraperConfig(BaseModel, table=False):
    """ Scraper configurations

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to False.
    """

    name : Optional[NameType] = None
    marketplace_id : Annotated[int, Field(foreign_key="marketplaces.id")]
    selectors : Annotated[Dict, Field(description="Json with selectors for scraping")]
    headers : Annotated[Dict, Field(description="request headers")]
    timeout_seconds : Optional[int] = None
    retry_attempts : Optional[int] = None




class Connector(BaseModel, table=False):
    """ Connector model

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to False.
    """

    name : NameType
    authentication_type : Annotated[Optional[str], Field(description="Type of authentication")]
    credentials : Annotated[str, Field(description="credentials for auth")]
    test_connection_status : Annotated[str, Field(description="Status of test connection, smth like keepalive")]
    last_connected_at : Annotated[Datetime, Field(description="Last time connection was alive")]


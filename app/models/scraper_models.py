from sqlmodel import Field, SQLModel
from typing import Optional, Annotated, Dict, List
from .base import BaseModel, NameType, Datetime


# Scraper related models 


class Scraper(BaseModel, table=True):
    """ Scraper model

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__="scrapers"

    name : NameType
    marketplace_id : Annotated[int, Field(foreign_key="marketplaces.id")]
    status : Annotated[str, Field(description="scraper status")]
    scraper_type : Annotated[str, Field(description="scraper type, e.g. Api, Web")]
    base_url : Annotated[str, Field(description="scraper base url")]



class ScraperSession(BaseModel, table=True):
    """ Session for scraper 

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """

    __tablename__="scraper_sessions"

    scraper_id : Annotated[int, Field(foreign_key="scrapers.id")]
    session_id : Optional[str] = None
    cookies : Annotated[Dict, Field(description="scraper session cookies")]
    headers : Annotated[Dict, Field(description="scraper session headers")]
    started_at : Datetime
    ended_at : Datetime
    requests_made : Annotated[List, Field(description="list of requests made")]
    requests_failed : Annotated[List, Field(description="list of requests failed")]



class ScrapingRule(BaseModel, table=True):
    """ Scraping rule

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """

    __tablename__="scraping_rules"

    scraper_instance_id : Annotated[int, Field(foreign_key="scrapers.id")]
    rule_type : Annotated[str, Field(description="Rule type : css_selector, xpath, regex, etc")]
    rule_name : Annotated[str, Field(description="name of the rule in the system")]
    extraction_type : Annotated[str, Field(description="Type of the output value, text, html etc")]
    attribute_name : Annotated[Optional[str], Field(description= )]


class ScrapedItem(BaseModel, table=True):
    pass 

class RateLimitRule(SQLModel, table=False):
    pass 


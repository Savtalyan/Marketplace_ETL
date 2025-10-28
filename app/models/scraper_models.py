from sqlmodel import Field, SQLModel, JSON
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
    cookies : Annotated[Dict[str, any], Field(description="scraper session cookies", sa_type=JSON)]
    headers : Annotated[Dict[str, any], Field(description="scraper session headers", sa_type=JSON)]
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
    attribute_name : Annotated[Optional[str], Field(description="If extracting attributes")]
    is_required : Annotated[Optional[bool], Field(description="Is the rule required or not")]
    validation_regex : Annotated[str, Field(description="regex for validation")]


class ScrapedItem(BaseModel, table=True):
    """ Instance of scraped item

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """

    __tablename__ = "scraped_items"

    scraping_job_id : Annotated[int, Field(foreign_key="etl_jobs.id")]
    item_url : Annotated[str, Field(description="URL of the scraped item")]
    scraped_data : Annotated[Dict, Field(description="scraped raw data in JSON format")]
    status : Annotated[str, Field(description="Status of the scraping")] # TODO implement the logic with enum
    http_status_code : Annotated[int, Field(description="status code of the extraction")]
    response_time : Annotated[int, Field(description="response time of the request")]
    error_message : Annotated[str, Field(max_length=100, description="error message while extraction")]
    retry_count : Annotated[int, Field(description="scraping retry count")]



class RateLimitRule(SQLModel, table=False):
    """ Rate limit rule instance

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """

    scraper_id : Annotated[int, Field(foreign_key="scrapers.id")]
    request_per_minute : Optional[int] = None
    request_per_hour : Optional[int] = None
    request_per_day : Optional[int] = None 
    domain_specific_limit : Annotated[Dict, Field(description="specific limits depending on domain")]
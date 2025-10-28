from sqlmodel import Field, Relationship
from typing import Optional, Annotated, List
from .base import BaseModel, NameType, StatusType

# Custom annotated types for reuse 





class ETLJob(BaseModel, table=True):
    """ Stored ETL jobs

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """

    __tablename__="etl_jobs"

    name : NameType
    status : StatusType
    started_at : Optional[datetime] = None
    completed_at : Optional[datetime] = None
    execution_time : Optional[int] = None
    total_records_processed : Optional[int] = None
    success_count : Optional[int] = None
    error_count : Optional[int] = None
    error_message : Annotated[Optional[str], Field(default=None, max_length=1000)]


    configurations : List["JobConfiguration"] = Relationship(back_populates="job")

class JobConfiguration(BaseModel, table=True):
    """ Configurations for each job which may differ

    Args:
        BaseModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """

    __tablename__ = "job_configurations"

    is_active : Optional[bool] = None
    marketplace_name : NameType
    storage_target : NameType
    job_id : Optional[int] = Field(foreign_key="etl_jobs.id")


    job : Optional[ETLJob] = Relationship(back_populates="configurations")





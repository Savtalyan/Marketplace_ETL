from pydantic_settings import BaseSettings
from typing import List
import os 


class Settings(BaseSettings):
    """Applications settings configuration"""

    # API configurations 

    APP_NAME : str = "Marketplace ETL API"
    HOST : str = "127.0.0.1"
    PORT : int = 8080
    DEBUG : bool = True 



    # cors configs 
    CORS_ORIGINS : List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]


    
    # TODO
    # implement database configurations here 


    # Logging configs 
    LOG_LEVEL : str = "INFO"


    class Config:
        env_file = ".env"
        case_sensitive = True


# create settings instance 
settings = Settings()
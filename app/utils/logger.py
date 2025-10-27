import logging 
import sys 
from app.core.config import settings 

def setup_logging(): 
    """Configure applicaiton logging"""

    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL),
        format="%(asctime)s = %(name)s, = %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            # in case of file logging implement FileHandler
        ]
    )


    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)

    
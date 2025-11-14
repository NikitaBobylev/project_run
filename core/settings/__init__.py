from .base import ENVIRONMENT

if ENVIRONMENT == "PRODUCTION": 
    from .production import *

else:
    from .local import *
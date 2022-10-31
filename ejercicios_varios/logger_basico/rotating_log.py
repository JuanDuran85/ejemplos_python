"""

    If you need to create a rotating log, you can do it with the built-in logging module

"""

import logging
from time import sleep
from logging.handlers import RotatingFileHandler

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

logger_root = logging.getLogger("Rotating Log")
logger_root.setLevel(logging.INFO)

handler_root = RotatingFileHandler("test.log", maxBytes=20, backupCount=2)

logger_root.addHandler(handler_root)

for i in range(15):
    logger_root.info(f"This is test log line {i}")
    sleep(1.5)


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
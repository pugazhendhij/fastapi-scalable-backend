import logging
from logging.handlers import RotatingFileHandler
import json

LOG_FILE = "logs/app.log"

def setup_logger():
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes= 5 * 1024 * 1024,
        backupCount = 5
    )

    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger
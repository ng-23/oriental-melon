import logging
from fastapi import FastAPI

app = FastAPI()
logger = logging.getLogger(name=__name__)

@app.get('/')
def root():
    logger.info('root endpoint called')
    return 'Hello world!'

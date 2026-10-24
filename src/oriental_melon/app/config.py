import logging
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import find_dotenv

logger = logging.getLogger(name=__name__)

class AppConfig(BaseSettings):
    '''
    Contains app-wide configuration information as stored in a .env file.
    '''
    # see https://fastapi.tiangolo.com/advanced/settings/#read-settings-from-env
    model_config = SettingsConfigDict(
        env_file=find_dotenv(filename='.env'),
        env_ignore_empty=True,
        extra='ignore',
    )

    API_VERSION: int = 1
    API_ROUTE_PREFIX: str = f'/api/v{API_VERSION}'

app_config = AppConfig()
logger.info('Instantiated AppConfig object')

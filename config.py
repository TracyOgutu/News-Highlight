import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCE_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}?api_key={}'
    ARTICLE_BASE_URL='https://newsapi.org/v2/everything?language=en&sources={}?api_key={}'
    API_KEY = os.environ.get('API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    @staticmethod
    def __init__app(app)

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}







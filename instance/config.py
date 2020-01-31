import os

class Config(object):
    """Parent configuration class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Configuration for Development"""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a seperate test database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TESTS')
    DEBUG = True

class StagingConfig(Config):
    """Configuration for Staging"""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production"""
    DEBUG = False
    Testing = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
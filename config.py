import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    GOOGLE_APPLICATION_CREDENTIAL = os.environ.get('GOOGLE_APPLICATION_CREDENTIAL')

class ProductionConfig(Config):
    GOOGLE_APPLICATION_CREDENTIAL = os.environ.get('GOOGLE_APPLICATION_CREDENTIAL')

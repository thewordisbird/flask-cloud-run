import os
from app import secrets_wrapper

class Config:
    PROJECT_ID = 'flask-cloud-run'
    SECRET_KEY = secrets_wrapper.access_secret_version(PROJECT_ID, 'SECRET_KEY')

class DevelopmentConfig(Config):
    GOOGLE_APPLICATION_CREDENTIAL = os.environ.get('GOOGLE_APPLICATION_CREDENTIAL')

class ProductionConfig(Config):
    #GOOGLE_APPLICATION_CREDENTIAL = os.environ.get('GOOGLE_APPLICATION_CREDENTIAL')

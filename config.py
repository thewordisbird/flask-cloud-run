import os
from app import secrets_wrapper

PROJECT_ID = 'flask-cloud-run'

class Config:    
    SECRET_KEY = secrets_wrapper.access_secret_version(PROJECT_ID, 'SECRET_KEY')

class DevelopmentConfig(Config):
    GOOGLE_APPLICATION_CREDENTIAL = secrets_wrapper.access_secret_version(PROJECT_ID, 'GOOGLE_APPLICATION_CREDENTIAL')

class ProductionConfig(Config):
    GOOGLE_APPLICATION_CREDENTIAL = secrets_wrapper.access_secret_version(PROJECT_ID, 'GOOGLE_APPLICATION_CREDENTIAL')

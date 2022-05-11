import os
from datetime import timedelta

from dotenv import load_dotenv

# Load .env file
ENV_PATH = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env')
load_dotenv(ENV_PATH)


class Config:
    """
    Base Configurations for the Project.
    """
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'].replace(
        'postgres://', 'postgresql://', 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    API_VERSION_STRING = '/api/v1'
    ENCRYPTION_SCHEMES = ['bcrypt']
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
    JWT_ALGORITHM = os.environ['JWT_ALGORITHM']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        seconds=int(os.environ['JWT_ACCESS_TOKEN_EXPIRES']))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        minutes=int(os.environ['JWT_REFRESH_TOKEN_EXPIRES']))
    CLOUDINARY_CLOUD_NAME = os.environ['CLOUDINARY_CLOUD_NAME']
    CLOUDINARY_CLOUD_API_KEY = os.environ['CLOUDINARY_CLOUD_API_KEY']
    CLOUDINARY_CLOUD_API_SECRET = os.environ['CLOUDINARY_CLOUD_API_SECRET']

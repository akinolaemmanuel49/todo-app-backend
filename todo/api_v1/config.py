import os

from dotenv import load_dotenv

# Load .env file
ENV_PATH = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env')
load_dotenv(ENV_PATH)


class Config:
    """
    Base Configurations for the Project.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace(
        'postgres://', 'postgresql://', 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    API_VERSION_STRING = '/api/v1'

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
    SECRET_KEY = os.environ('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False

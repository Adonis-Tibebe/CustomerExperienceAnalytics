"""
Configuration settings for the application.
"""

# Add your configuration here
import os
from dotenv import load_dotenv

def get_base_data_dir(env_file_path='../.env'):
    """
    Loads BASE_DATA_DIR from .env file.
    Returns the path as a string.
    """
    dotenv_path = os.path.join(os.path.dirname(__file__), env_file_path)
    load_dotenv(dotenv_path)

    base_dir = os.getenv('BASE_DATA_DIR')
    if not base_dir:
        raise ValueError("🚨 BASE_DATA_DIR not set in .env file.")
    
    return base_dir

def get_db_credentials(env_path = "../.env"):
    dotenv_path = os.path.join(os.path.dirname(__file__), env_path)
    load_dotenv(dotenv_path)

    ORACLE_CONFIG = {
    "username": os.getenv("ORACLE_USERNAME"),
    "password": os.getenv("ORACLE_PASSWORD"),
    "host": os.getenv("ORACLE_HOST", "localhost"),
    "port": os.getenv("ORACLE_PORT", "1521"),
    "service_name": os.getenv("ORACLE_SERVICE", "XEPDB1")
    }
    return ORACLE_CONFIG
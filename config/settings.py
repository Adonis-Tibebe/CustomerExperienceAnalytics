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

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    

def clean_data(df, date_columns=None):
    """
    Cleans the dataframe by:
    - Dropping duplicate rows
    - Removing rows with null values
    - Parsing date columns into datetime format
    """
    df = df.drop_duplicates()
    df = df.dropna()

    if date_columns:
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    
    return df

import re
def clean_review_text(text):
    """
    Lightweight cleaning for DistilBERT:
    - Removes HTML, URLs, and mentions
    - Preserves emojis, punctuation, contractions
    """
    if not isinstance(text, str):
        return ""

    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text




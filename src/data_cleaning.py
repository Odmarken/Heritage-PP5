import pandas as pd

def clean_data(file_path):
    """
    Cleans the dataset by handling missing values, 
    removing unnecessary columns, and ensuring valid data.

    This function loads a dataset, processes it to ensure all the data
    is usable, and returns a cleaned version of the dataset.

    Args:
        file_path (str): Path to the raw dataset file (e.g., "inputs/datasets/raw/dataset.csv").

    Returns:
        pd.DataFrame: A cleaned dataset ready for further processing or analysis.
    """

    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully from {file_path}")
    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}. Make sure the path is correct.")
        raise e
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        raise e

 
    print(f"Initial dataset shape: {df.shape}")
    df = df.dropna()
    print(f"Shape after dropping missing values: {df.shape}")

   
    if 'ID' in df.columns:
        df = df.drop(columns=['ID'])
        print("Dropped 'ID' column.")

  
    if 'price' in df.columns:
        original_rows = df.shape[0]
        df = df[df['price'] > 0]
        cleaned_rows = df.shape[0]
        print(f"Removed {original_rows - cleaned_rows} rows with negative or zero prices.")
    else:
        print("Warning: 'price' column not found. Skipping price validation.")

 
    print(f"Final dataset shape: {df.shape}")
    return df

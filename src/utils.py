"""
Utility functions for data processing and analysis.
"""

import pandas as pd
import numpy as np


def read_csv_safe(filepath, **kwargs):
    """
    Safe CSV reader with error handling.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
    **kwargs : dict
        Additional arguments to pass to pd.read_csv()
    
    Returns:
    --------
    pd.DataFrame or None
        Loaded dataframe or None if error occurs
    """
    try:
        df = pd.read_csv(filepath, **kwargs)
        print(f"✓ Successfully loaded {len(df)} rows and {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        print(f"✗ File not found: {filepath}")
        return None
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        return None


def get_data_info(df, name="DataFrame"):
    """
    Print basic information about the dataframe.
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataframe to analyze
    name : str
        Name to display for the dataframe
    """
    print(f"\n=== {name} Information ===")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Data types:\n{df.dtypes}")
    print(f"Missing values:\n{df.isnull().sum()}")


if __name__ == "__main__":
    print("Utility functions loaded successfully!")
    print("Available functions:")
    print("- read_csv_safe(filepath)")
    print("- get_data_info(df)")

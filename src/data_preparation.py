"""
data_cleaning.py

"""

import pandas as pd


def load_dataset(filepath):
    #Load the dataset into a Pandas DataFrame.

    print("\nLoading dataset...")
    df = pd.read_csv(filepath)
    print("Dataset loaded successfully.")

    return df


def inspect_dataset(df):
    #Display basic information about the dataset.
    

    print("\nDataset Information")
    print("-" * 40)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nMachine Failure Values:")
    print(df["Machine failure"].unique())


def clean_dataset(df):
    """
    Perform data cleaning:
    - Remove duplicates
    - Fill missing values
    - Verify Machine failure values
    """

    print("\nCleaning dataset...")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        df = df.drop_duplicates()
        print(f"Removed {duplicates} duplicate rows.")
    else:
        print("No duplicate rows found.")

    # Fill missing numeric values
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        if df[column].isnull().sum() > 0:
            median = df[column].median()
            df[column] = df[column].fillna(median)

    # Fill missing categorical values
    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            mode = df[column].mode()[0]
            df[column] = df[column].fillna(mode)

    # Verify Machine failure values
    valid_values = {0, 1}
    values = set(df["Machine failure"].unique())

    if values.issubset(valid_values):
        print("Machine failure column verified.")
    else:
        raise ValueError("Invalid values detected in Machine failure column.")

    print("Dataset cleaned successfully.")

    return df


def save_cleaned_data(df, filepath):
    """
    Save cleaned dataset.
    """

    df.to_csv(filepath, index=False)
    print(f"Cleaned dataset saved to: {filepath}")
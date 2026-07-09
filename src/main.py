"""
main.py

Entry point for the Predictive Maintenance Analysis project.
Loads the dataset, performs data cleaning, and saves the cleaned data.
"""

from data_cleaning import (
    load_dataset,
    inspect_dataset,
    clean_dataset,
    save_cleaned_data
)


def main():
    print("=" * 60)
    print("Predictive Maintenance Analysis")
    print("=" * 60)

    # Load dataset
    df = load_dataset("dataset/ai4i2020.csv")

    # Inspect dataset
    inspect_dataset(df)

    # Clean dataset
    cleaned_df = clean_dataset(df)

    # Save cleaned dataset
    save_cleaned_data(cleaned_df, "outputs/cleaned_data.csv")

    print("\nData cleaning completed successfully.")
    print("Cleaned dataset saved to outputs/cleaned_data.csv")


if __name__ == "__main__":
    main()
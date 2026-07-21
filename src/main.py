"""
main.py

Entry point for the Predictive Maintenance Analysis project.
Loads the dataset, performs data cleaning, and saves the cleaned data.
"""

from data_preparation import (
    load_dataset,
    inspect_dataset,
    clean_dataset,
    save_cleaned_data
)
from analysis import calculate_kpis, print_kpis, save_kpis
from exploratory_analysis import run_exploratory_analysis


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
    
    # Calculate KPIs
    kpis = calculate_kpis(cleaned_df)

    # Display KPIs
    print_kpis(kpis)
    save_kpis(kpis, "outputs/kpis.csv")
    
    # Exploratory Data Analysis
    run_exploratory_analysis(cleaned_df)

    print("Cleaned dataset saved to outputs/cleaned_data.csv")
    print("KPIs saved to: outputs/kpis.csv")
    print("EDA figures saved to: outputs/figures/")



if __name__ == "__main__":
    main()
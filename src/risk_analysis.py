"""
Risk Analysis
Predictive Maintenance Analysis for Industrial Equipment
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

OUTPUT_DIR = "outputs/figures"
ANALYSIS_DIR = "outputs/analysis"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ANALYSIS_DIR, exist_ok=True)


def run_risk_analysis(df):
    """
    Create a simple risk score and classify machines into
    Low, Medium, and High Risk categories.
    """

    print("=" * 50)
    print("Risk Analysis")
    print("=" * 50)

    # ---------------------------------------------
    # Create Categories
    # ---------------------------------------------

    df["Tool Wear Category"] = pd.cut(
        df["Tool wear [min]"],
        bins=[0, 100, 200, df["Tool wear [min]"].max()],
        labels=["Low", "Medium", "High"],
        include_lowest=True,
    )

    df["Speed Category"] = pd.qcut(
        df["Rotational speed [rpm]"],
        q=3,
        labels=["Low", "Medium", "High"],
    )

    df["Torque Category"] = pd.qcut(
        df["Torque [Nm]"],
        q=3,
        labels=["Low", "Medium", "High"],
    )

    # ---------------------------------------------
    # Risk Score
    # ---------------------------------------------

    df["Risk Score"] = 0

    df.loc[df["Tool Wear Category"] == "High", "Risk Score"] += 1
    df.loc[df["Torque Category"] == "High", "Risk Score"] += 1
    df.loc[df["Speed Category"] == "Low", "Risk Score"] += 1
    df.loc[df["Process temperature [K]"] > 311, "Risk Score"] += 1

    # ---------------------------------------------
    # Risk Category
    # ---------------------------------------------

    df["Risk Category"] = pd.cut(
        df["Risk Score"],
        bins=[-1, 1, 3, 4],
        labels=["Low", "Medium", "High"],
    )

    # ---------------------------------------------
    # Risk Summary
    # ---------------------------------------------

    risk_summary = (
        df["Risk Category"]
        .value_counts()
        .rename_axis("Risk Category")
        .reset_index(name="Machines")
    )

    print("\nRisk Distribution")
    print(risk_summary)

    risk_summary.to_csv(
        f"{ANALYSIS_DIR}/risk_analysis.csv",
        index=False
    )

    # ---------------------------------------------
    # Failure Rate by Risk
    # ---------------------------------------------

    failure_rate = (
        df.groupby("Risk Category")["Machine failure"]
        .mean()
        .mul(100)
        .reset_index(name="Failure Rate (%)")
    )

    print("\nFailure Rate by Risk")
    print(failure_rate)

    failure_rate.to_csv(
        f"{ANALYSIS_DIR}/failure_rate_by_risk.csv",
        index=False
    )

    # ---------------------------------------------
    # Risk Distribution Chart
    # ---------------------------------------------

    plt.figure(figsize=(7, 5))

    sns.countplot(
        data=df,
        x="Risk Category",
        order=["Low", "Medium", "High"]
    )

    plt.title("Risk Category Distribution")
    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/risk_distribution.png",
        dpi=300
    )

    plt.close()

    # ---------------------------------------------
    # Failure Rate Chart
    # ---------------------------------------------

    plt.figure(figsize=(7, 5))

    sns.barplot(
        data=failure_rate,
        x="Risk Category",
        y="Failure Rate (%)",
        order=["Low", "Medium", "High"]
    )

    plt.title("Failure Rate by Risk Category")
    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_DIR}/failure_rate_by_risk.png",
        dpi=300
    )

    plt.close()

    print("\nAnalysis files saved to:")
    print(f"  {ANALYSIS_DIR}/risk_analysis.csv")
    print(f"  {ANALYSIS_DIR}/failure_rate_by_risk.csv")

    print("\nFigures saved to:")
    print(f"  {OUTPUT_DIR}/risk_distribution.png")
    print(f"  {OUTPUT_DIR}/failure_rate_by_risk.png")

    print("\nRisk analysis completed successfully.")

    return df
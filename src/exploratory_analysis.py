"""
Exploratory Analysis
Predictive Maintenance Analysis for Industrial Equipment
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

OUTPUT_DIR = "outputs/figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def run_exploratory_analysis(df):
    """
    Perform exploratory data analysis on the cleaned dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Cleaned predictive maintenance dataset.
    """

    print("=" * 50)
    print("Exploratory Data Analysis")
    print("=" * 50)

    print("\nDataset Shape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nMachine Failure Distribution")
    print(df["Machine failure"].value_counts())

    # -------------------------------------------------------
    # 1. Failure Rate by Machine Type
    # -------------------------------------------------------

    machine_failure = (
        df.groupby("Type")["Machine failure"]
        .mean()
        .mul(100)
        .reset_index(name="Failure Rate (%)")
    )

    plt.figure(figsize=(8, 5))
    sns.barplot(data=machine_failure, x="Type", y="Failure Rate (%)")
    plt.title("Failure Rate by Machine Type")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/failure_by_machine_type.png", dpi=300)
    plt.close()

    print(machine_failure)

    # -------------------------------------------------------
    # 2. Tool Wear Category
    # -------------------------------------------------------

    df["Tool Wear Category"] = pd.cut(
        df["Tool wear [min]"],
        bins=[0, 100, 200, df["Tool wear [min]"].max()],
        labels=["Low", "Medium", "High"],
        include_lowest=True,
    )

    toolwear = (
        df.groupby("Tool Wear Category")["Machine failure"]
        .mean()
        .mul(100)
        .reset_index(name="Failure Rate (%)")
    )

    plt.figure(figsize=(8, 5))
    sns.barplot(data=toolwear, x="Tool Wear Category", y="Failure Rate (%)")
    plt.title("Failure Rate by Tool Wear Category")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/failure_by_tool_wear.png", dpi=300)
    plt.close()

    print(toolwear)

    # -------------------------------------------------------
    # 3. Rotational Speed Category
    # -------------------------------------------------------

    df["Speed Category"] = pd.qcut(
        df["Rotational speed [rpm]"],
        q=3,
        labels=["Low", "Medium", "High"],
    )

    speed = (
        df.groupby("Speed Category")["Machine failure"]
        .mean()
        .mul(100)
        .reset_index(name="Failure Rate (%)")
    )

    plt.figure(figsize=(8, 5))
    sns.barplot(data=speed, x="Speed Category", y="Failure Rate (%)")
    plt.title("Failure Rate by Rotational Speed Category")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/failure_by_speed.png", dpi=300)
    plt.close()

    print(speed)

    # -------------------------------------------------------
    # 4. Torque Category
    # -------------------------------------------------------

    df["Torque Category"] = pd.qcut(
        df["Torque [Nm]"],
        q=3,
        labels=["Low", "Medium", "High"],
    )

    torque = (
        df.groupby("Torque Category")["Machine failure"]
        .mean()
        .mul(100)
        .reset_index(name="Failure Rate (%)")
    )

    plt.figure(figsize=(8, 5))
    sns.barplot(data=torque, x="Torque Category", y="Failure Rate (%)")
    plt.title("Failure Rate by Torque Category")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/failure_by_torque.png", dpi=300)
    plt.close()

    print(torque)

    # -------------------------------------------------------
    # 5. Temperature Comparison
    # -------------------------------------------------------

    temperature = df.melt(
        id_vars="Machine failure",
        value_vars=[
            "Air temperature [K]",
            "Process temperature [K]",
        ],
        var_name="Temperature Type",
        value_name="Temperature",
    )

    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=temperature,
        x="Temperature Type",
        y="Temperature",
        hue="Machine failure",
    )
    plt.title("Temperature Comparison")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/temperature_comparison.png", dpi=300)
    plt.close()

    summary = (
        df.groupby("Machine failure")[
            ["Air temperature [K]", "Process temperature [K]"]
        ]
        .describe()
    )

    print(summary)

    print("\nExploratory Analysis Completed Successfully.")
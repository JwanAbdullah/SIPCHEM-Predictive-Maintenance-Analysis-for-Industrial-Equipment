"""
analysis.py

Calculates Key Performance Indicators (KPIs)
for the Predictive Maintenance dataset.
"""

import pandas as pd


def calculate_kpis(df):
    """
    Calculate the required KPIs.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
        Dictionary containing KPI values.
    """

    total_records = len(df)

    total_failures = df["Machine failure"].sum()
    failure_rate = (total_failures / total_records) * 100
    average_tool_wear = df["Tool wear [min]"].mean()
    average_torque = df["Torque [Nm]"].mean()
    average_rotational_speed = df["Rotational speed [rpm]"].mean()

    kpis = {
        "Total Records": total_records,
        "Total Failures": total_failures,
        "Failure Rate (%)": failure_rate,
        "Average Tool Wear": average_tool_wear,
        "Average Torque": average_torque,
        "Average Rotational Speed": average_rotational_speed,
    }

    return kpis


def print_kpis(kpis):
    """
    Display KPIs in a readable format.
    """

    print("\n" + "=" * 60)
    print("KEY PERFORMANCE INDICATORS")
    print("=" * 60)

    print(f"Total Records           : {kpis['Total Records']:,}")
    print(f"Total Failures          : {kpis['Total Failures']:,}")
    print(f"Failure Rate            : {kpis['Failure Rate (%)']:.2f}%")
    print(f"Average Tool Wear       : {kpis['Average Tool Wear']:.2f} min")
    print(f"Average Torque          : {kpis['Average Torque']:.2f} Nm")
    print(f"Average Rotational Speed: {kpis['Average Rotational Speed']:.2f} rpm")
    
    
def save_kpis(kpis, filepath):
    """
    Save KPIs to a CSV file.
    """

    import pandas as pd

    kpi_df = pd.DataFrame(
        list(kpis.items()),
        columns=["KPI", "Value"]
    )

    kpi_df.to_csv(filepath, index=False)

    print(f"\nKPIs saved to: {filepath}")
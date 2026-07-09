# KPI Calculation

## Purpose

This stage calculates the key performance indicators (KPIs) required for the Predictive Maintenance Analysis project. These metrics provide a high-level overview of the dataset and establish baseline values for subsequent exploratory data analysis and risk assessment.

---

## KPIs

| KPI | Value |
|------|------:|
| Total Records | 10,000 |
| Total Machine Failures | 339 |
| Failure Rate | 3.39% |
| Average Tool Wear | 107.95 min |
| Average Torque | 39.99 Nm |
| Average Rotational Speed | 1538.78 rpm |

---

## Implementation

The KPIs were calculated using **Python** and **Pandas** after completing the data preparation stage. Calculations were performed on the cleaned dataset to ensure accuracy and consistency.

The following metrics were computed:

- Total number of machine records
- Total number of machine failures
- Overall failure rate
- Average tool wear
- Average torque
- Average rotational speed

---

## Business Importance

These KPIs provide baseline measurements of machine performance and reliability. They will be used to:

- Support exploratory data analysis.
- Compare machine operating conditions.
- Build the machine risk scoring model.
- Create dashboard KPI cards.
- Support business recommendations for preventive maintenance.

---

## Output

The KPI results are:

- Displayed in the terminal.
- Saved to `outputs/kpis.csv`.
- Used in subsequent analysis stages.

---

## Summary

The KPI calculation stage successfully established the baseline performance metrics required for the project. These results form the foundation for the exploratory analysis and risk classification that follow.
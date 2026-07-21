# Risk Analysis

## Objective

The objective of this analysis is to classify machines into Low, Medium, and High Risk categories using operational indicators observed during exploratory analysis.

---

## Risk Factors

The following factors were used to calculate the risk score:

- High tool wear
- High torque
- Low rotational speed
- High process temperature

Each condition contributes one point to the overall risk score.

---

## Risk Categories

| Risk Score | Category |
|------------|----------|
| 0–1 | Low |
| 2–3 | Medium |
| 4 | High |

---

## Analysis Performed

### Risk Category Distribution

Calculated the number of machines classified as Low, Medium, and High Risk.

### Failure Rate by Risk Category

Compared the machine failure rate across the three risk categories.

---

## Generated Outputs

### CSV Files

- risk_analysis.csv
- failure_rate_by_risk.csv

### Figures

- risk_distribution.png
- failure_rate_by_risk.png
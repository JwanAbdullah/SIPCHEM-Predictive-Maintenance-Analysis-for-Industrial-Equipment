# Data Cleaning Documentation

## Purpose

The purpose of the data cleaning stage is to ensure that the dataset is accurate, complete, and suitable for analysis.

A clean dataset improves the reliability of calculated KPIs, statistical summaries, visualizations, and risk classification.

---

# Cleaning Checklist

| Task | Status | Notes |
|------|:------:|------|
| Dataset Loaded | ☐ | |
| Checked Missing Values | ☐ | |
| Checked Duplicate Records | ☐ | |
| Verified Data Types | ☐ | |
| Verified Machine Failure Values | ☐ | |
| Saved Clean Dataset | ☐ | |

---

# Dataset Inspection

## Number of Records

To be completed after loading the dataset.

## Number of Columns

To be completed after loading the dataset.

## Column Names

- UDI
- Product ID
- Type
- Air temperature [K]
- Process temperature [K]
- Rotational speed [rpm]
- Torque [Nm]
- Tool wear [min]
- Machine failure
- TWF
- HDF
- PWF
- OSF
- RNF

---

# Missing Value Check

Method

```python
df.isnull().sum()
```

### Result

_To be completed after analysis._

Example:

```
No missing values were detected.
```

or

```
Two missing values were found in Tool Wear and replaced with the column median.
```

---

# Duplicate Record Check

Method

```python
df.duplicated().sum()
```

### Result

_To be completed after analysis._

Example

```
No duplicate records were found.
```

or

```
Five duplicate rows were removed.
```

---

# Data Type Validation

Each column will be inspected using:

```python
df.info()
```

The objective is to confirm that:

- Numeric columns are stored as numeric data types.
- Categorical columns are stored as object/category.
- No unexpected data type conversions exist.

---

# Machine Failure Validation

The Machine Failure column should contain only:

| Value | Meaning |
|-------:|---------|
| 0 | No Failure |
| 1 | Failure |

Validation Method

```python
df["Machine failure"].unique()
```

Expected Output

```
[0, 1]
```

---

# Data Cleaning Decisions

This section will record any modifications made during cleaning.

| Issue | Action Taken | Reason |
|------|--------------|--------|
| None | None | Dataset already clean |

*(Update this table if any issues are discovered during analysis.)*

---

# Clean Dataset

Output File

```
outputs/cleaned_data.csv
```

---

# Summary

After completing the cleaning process, the dataset will be ready for:

- KPI calculation
- Exploratory Data Analysis (EDA)
- Risk score calculation
- Data visualization
- Business recommendation development

Any cleaning decisions will be documented in this file to ensure transparency and reproducibility.
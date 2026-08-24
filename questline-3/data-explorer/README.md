# Data Explorer - Students Performance Dataset

## Overview
Initial exploratory data analysis performed using Python and Pandas on the Students Performance Dataset.

## Results

### 1. Dataset Shape
- **Shape**: `(1000, 8)`
- **Total Rows**: 1000
- **Total Columns**: 8

### 2. Columns List
- `gender`
- `race/ethnicity`
- `parental level of education`
- `lunch`
- `test preparation course`
- `math score`
- `reading score`
- `writing score`

### 3. Data Types
- `gender`: `object` (Categorical)
- `race/ethnicity`: `object` (Categorical)
- `parental level of education`: `object` (Categorical)
- `lunch`: `object` (Categorical)
- `test preparation course`: `object` (Categorical)
- `math score`: `int64` (Numerical)
- `reading score`: `int64` (Numerical)
- `writing score`: `int64` (Numerical)

### 4. Missing Values
- No missing or null values found (`df.isnull().sum()` is 0 for all columns).

### 5. Summary Statistics (Numerical Features)
- **Math Score**: Mean ≈ 66.09, Std ≈ 15.16, Min = 0, Max = 100
- **Reading Score**: Mean ≈ 69.17, Std ≈ 14.60, Min = 17, Max = 100
- **Writing Score**: Mean ≈ 68.05, Std ≈ 15.20, Min = 10, Max = 100

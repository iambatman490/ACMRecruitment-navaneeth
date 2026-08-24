import pandas as pd

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# 1. Dataset Shape
print("=== Dataset Shape ===")
print(df.shape)

# 2. List Columns
print("\n=== Columns ===")
print(df.columns.tolist())

# 3. Data Types
print("\n=== Data Types ===")
print(df.dtypes)

# 4. Missing Values
print("\n=== Missing Values ===")
print(df.isnull().sum())

# 5. Summary Statistics
print("\n=== Summary Statistics ===")
print(df.describe())

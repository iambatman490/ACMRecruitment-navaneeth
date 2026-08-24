import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print("=== Dataset Shape ===")
print(f"Shape: {df.shape} (Rows: {df.shape[0]}, Columns: {df.shape[1]})\n")
print("=== Columns ===")
for col in df.columns:
    print(f"- {col}")
print()
print("=== Data Types ===")
print(df.dtypes)

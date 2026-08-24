import pandas as pd
# 1. Load datase
df = pd.read_csv('StudentsPerformance.csv')
print("Initial Shape:", df.shape)
missing_count = df.isnull().sum().sum()
print(f"Total missing values found: {missing_count}")
initial_rows = len(df)
df = df.drop_duplicates()
print(f"Removed {initial_rows - len(df)} duplicate records.")
assert df.duplicated().sum() == 0, "Duplicates exist!"
assert df.isnull().sum().sum() == 0, "Missing values exist!"
print("Verification complete: Dataset is clean.")
print("Final Shape:", df.shape)
df.to_csv('cleaned_students_performance.csv', index=False)
print("Saved as cleaned_students_performance.csv")



## Objective
Transform the raw Students Performance dataset into a clean and reliable dataset by handling missing values, removing duplicate records, and ensuring data integrity.

1. **Loading the Dataset**:
   - Loaded `StudentsPerformance.csv` into a Pandas DataFrame.
2. **Handling Missing Values**:
   - Checked each column for null/missing values using `.isnull().sum()`.
   - Verified that the dataset contains 0 missing entries.
3. **Removing Duplicates**:
   - Checked for duplicate rows using `.duplicated()`.
   - Applied `.drop_duplicates()` to ensure row uniqueness.
4. **Integrity Verification**:
   - Verified that total duplicate count is 0 and null count is 0 using assertions.
5. **Saving Cleaned Dataset**:
   - Exported the finalized cleaned data to `cleaned_students_performance.csv`.

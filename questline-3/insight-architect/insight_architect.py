import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")
sns.set_theme(style="whitegrid")

# 1. Histogram: Distribution of Math Scores
plt.figure(figsize=(8, 5))
sns.histplot(df["math score"], kde=True, color="teal", bins=20)
plt.title("Distribution of Math Scores", fontsize=14)
plt.xlabel("Math Score", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.tight_layout()
plt.savefig("hist_math_score.png")
plt.close()

# 2. Bar Chart: Average Scores by Parental Level of Education
plt.figure(figsize=(10, 5))
parent_order = [
    "some high school",
    "high school",
    "some college",
    "associate's degree",
    "bachelor's degree",
    "master's degree",
]
sns.barplot(
    data=df,
    x="parental level of education",
    y="math score",
    order=parent_order,
    palette="Blues_d",
)
plt.title("Average Math Score by Parental Level of Education", fontsize=14)
plt.xlabel("Parental Level of Education", fontsize=12)
plt.ylabel("Average Math Score", fontsize=12)
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("bar_parental_education.png")
plt.close()

# 3. Box Plot: Scores by Test Preparation Course
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="test preparation course",
    y="reading score",
    palette="Set2",
)
plt.title("Reading Score Distribution by Test Preparation Course", fontsize=14)
plt.xlabel("Test Preparation Course", fontsize=12)
plt.ylabel("Reading Score", fontsize=12)
plt.tight_layout()
plt.savefig("box_test_prep.png")
plt.close()

# 4. Scatter Plot: Reading Score vs Writing Score with Gender Hue
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="reading score",
    y="writing score",
    hue="gender",
    alpha=0.7,
    palette="coolwarm",
)
plt.title("Reading Score vs. Writing Score by Gender", fontsize=14)
plt.xlabel("Reading Score", fontsize=12)
plt.ylabel("Writing Score", fontsize=12)
plt.tight_layout()
plt.savefig("scatter_reading_writing.png")
plt.close()

# 5. Heatmap: Correlation Matrix of Exam Scores
plt.figure(figsize=(7, 5))
corr = df[["math score", "reading score", "writing score"]].corr()
sns.heatmap(corr, annot=True, cmap="mako", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Exam Scores", fontsize=14)
plt.tight_layout()
plt.savefig("heatmap_correlations.png")
plt.close()

print("All 5 visualizations generated and saved successfully.")

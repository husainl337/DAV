import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
# print(df.head())


missing_vals = df.isnull().sum()
print(missing_vals)

df_clean = df.drop_duplicates()
print("\nDataFrame shape after dropping duplicates:", df_clean.shape)

num_cols = df_clean.select_dtypes(include=[np.number]).columns
print("\nNumerical columns considered for outlier detection:", list(num_cols))

# Detect outliers based on IQR for each numerical column
def detect_outliers_iqr(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (data[col] < lower_bound) | (data[col] > upper_bound)

# Create a DataFrame to hold outlier flags for each numerical column
outlier_flags = pd.DataFrame()
for col in num_cols:
    outlier_flags[col] = detect_outliers_iqr(df_clean, col)

# Count outliers per row
outlier_flags['outlier_count'] = outlier_flags.sum(axis=1)

# Remove rows having more than two outliers
df_no_outliers = df_clean[outlier_flags['outlier_count'] <= 2]
print("\nDataFrame shape after removing rows with more than two outliers:", df_no_outliers.shape)

# Optional: Plot boxplots before and after cleaning (for one feature e.g. 'age')
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(x=df_clean['age'])
plt.title("Age - Before Outlier Removal")

plt.subplot(1, 2, 2)
sns.boxplot(x=df_no_outliers['age'])
plt.title("Age - After Outlier Removal")
plt.show()

# Step 4: Correlation matrix and find most correlated positive and negative pairs
corr_matrix = df_no_outliers[num_cols].corr()
print("\nCorrelation matrix:\n", corr_matrix)

# Extract upper triangle of the correlation matrix without diagonal
upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
# Find the most positively correlated pair
max_corr = upper_tri.max().max()
max_pair = [(col, row) for col in upper_tri.columns for row in upper_tri.index if upper_tri.loc[row, col] == max_corr]

# Find the most negatively correlated pair
min_corr = upper_tri.min().min()
min_pair = [(col, row) for col in upper_tri.columns for row in upper_tri.index if upper_tri.loc[row, col] == min_corr]
print(f"\nMost positively correlated attributes: {max_pair} with correlation {max_corr:.3f}")
print(f"Most negatively correlated attributes: {min_pair} with correlation {min_corr:.3f}")

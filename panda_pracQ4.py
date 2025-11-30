import pandas as pd
import numpy as np
from sklearn import datasets
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

iris = datasets.load_iris()
df = pd.DataFrame(data = iris.data, columns=iris.feature_names)
# print(df.head())

# Mean 
mean_vals = df.iloc[: , :].mean()
print(mean_vals)

# # Mode 
mode_vals = df.iloc[: , :].mean().iloc[0]
print(mode_vals)

# Median 
med_vals = df.iloc[: , :].median()
print(med_vals)

# Standard variation 
std_vals = df.iloc[: , :].std()
print(std_vals)

# Standard error 
st_error = df.iloc[: , :].sem()
print(st_error)

# 95% Confidence Interval
conf_int = {}
for col in df.columns[:-1]:
    mean = df[col].mean()
    se = df[col].sem()
    ci = stats.t.interval(0.95, len(df[col])-1, loc=mean, scale=se)
    conf_int[col] = ci
print("\n95% Confidence Intervals:")
for col, ci in conf_int.items():
    print(f"{col}: {ci}")

# (b) Correlation Coefficients + Heatmap
print("\n(b) Correlation Matrix:")

corr_matrix = df.iloc[: , :].corr()
print(corr_matrix)

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Heatmap of Feature Correlations")
plt.show()

# (c) Covariance: Sepal Length vs Petal Length
print("\n(c) Covariance between Sepal Length and Petal Length:")

cov_matrix = np.cov(df["sepal length (cm)"], df["petal length (cm)"])
cov_val = cov_matrix[0, 1]
print("Covariance:", cov_val)

# (d) Contingency Table for Class Feature
print("\n(d) Contingency Table:")

contingency_table = pd.crosstab(index=df['species'], columns="count")
print(contingency_table)




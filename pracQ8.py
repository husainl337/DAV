import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np

# Load dataset 
df = sns.load_dataset('penguins') 

# Identify numeric and categorical columns 
numeric_features = df.select_dtypes(include=[np.number]).columns 
categorical_features = df.select_dtypes(include=['object', 'category']).columns 
print("Number of numeric features:", len(numeric_features)) 
print("Number of categorical features:", len(categorical_features)) 
print("Numeric features:", list(numeric_features)) 
print("Categorical features:", list(categorical_features)) 

# Correlation matrix 
corr_matrix = df[numeric_features].corr() 
print("Correlation matrix:\n", corr_matrix) 

# Example: if correlation > 0.8, drop one column 
# Here, let's check for correlations > 0.8 (excluding self-correlation) 
high_corr = np.where((corr_matrix.abs() > 0.8) & (corr_matrix.abs() < 1)) 
high_corr_pairs = [(numeric_features[i], numeric_features[j]) for i,j in zip(*high_corr) if i < j] 
print("Highly correlated pairs:", high_corr_pairs) 
# If any, remove the second column of the first pair 
if high_corr_pairs: 
    col_to_drop = high_corr_pairs[0][1] 
    df = df.drop(columns=[col_to_drop]) 
    print(f"Dropped column '{col_to_drop}' due to high correlation") 
    # Update numeric_features after dropping the column 
    numeric_features = df.select_dtypes(include=[np.number]).columns 

# Five-number summary 
five_num_summary = df[numeric_features].describe().loc[['min','25%','50%','75%','max']] 
print("Five-number summary:\n", five_num_summary) 

# Visualize using boxplots 
plt.figure(figsize=(10,6)) 
df[numeric_features].boxplot() 
plt.title("Boxplot of Numeric Features") 
plt.ylabel("Value") 
plt.show() 
df[numeric_features].hist(figsize=(12,6), bins=15) 
plt.suptitle("Histogram of Numeric Features") 
plt.show()
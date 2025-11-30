
from sklearn.datasets import fetch_openml 
import matplotlib.pyplot as plt
import seaborn as sns

titanic = fetch_openml('titanic',  version=1,  as_frame=True)
df = titanic.frame

# Count survivors by gender 
survivor_counts = df.groupby(['sex', 'survived']).size().unstack()
# Plot 
survivor_counts.plot(kind='bar', figsize=(8,6)) 
plt.title('Survivor Count by Gender') 
plt.xlabel('Gender') 
plt.ylabel('Number of Passengers') 
plt.legend(['Did Not Survive', 'Survived']) 
plt.show()

# Drop missing values for scatter plot 
df_scatter = df[['age', 'fare']].dropna() 
plt.figure(figsize=(8,6)) 
plt.scatter(df_scatter['age'], df_scatter['fare'], alpha=0.5, c='teal', edgecolor='k') 
plt.title('Scatter Plot of Age vs Fare') 
plt.xlabel('Age') 
plt.ylabel('Fare') 
plt.show() 

plt.figure(figsize=(10,5)) 
sns.kdeplot(df['age'].dropna(), label='Age', fill=True) 
sns.kdeplot(df['fare'].dropna(), label='Fare', fill=True) 
plt.title('Density Distribution of Age and Fare') 
plt.xlabel('Value') 
plt.ylabel('Density') 
plt.legend() 
plt.show()

numeric_features = ['age', 'fare', 'pclass', 'survived'] 
sns.pairplot(df[numeric_features].dropna(), hue='survived', palette='Set1', diag_kind='kde') 
plt.suptitle('Pairwise Bivariate Distribution', y=1.02) 
plt.show()
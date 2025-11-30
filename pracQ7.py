from sklearn.datasets import fetch_openml 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

titanic = fetch_openml('titanic',  version=1,  as_frame=True)
df = titanic.frame

# Convert 'survived' column to numeric 
df['survived'] = pd.to_numeric(df['survived'])

# Drop missing ages before filtering 
num_passengers_under_30 = df[df['age'].notna() & (df['age'] < 30)].shape[0] 
print("Total number of passengers with age less than 30:", num_passengers_under_30) 

total_fare_first_class = df[df['pclass'] == 1]['fare'].sum() 
print("Total fare paid by first-class passengers:", total_fare_first_class) 

survivors_by_class = df[df['survived'] == 1].groupby('pclass').size() 
print("Number of survivors by passenger class:") 
print(survivors_by_class) 

survivors_by_class.plot(kind='bar', color=['gold','silver','brown']) 
plt.title('Number of Survivors by Passenger Class') 
plt.xlabel('Passenger Class') 
plt.ylabel('Number of Survivors') 
plt.show()
import pandas as pd
import numpy as np


df = pd.read_csv("dff.csv")
# print(df)

group_name = df.groupby("Name")
# print(group_name["MonthlyIncome (Rs.)"].sum())

# print("lowest income is: \n",group_name["MonthlyIncome (Rs.)"].min())
# print("highest income is: \n",group_name["MonthlyIncome (Rs.)"].max())

low_income = df[df["MonthlyIncome (Rs.)"] < 80000]
# print(low_income)

female = df[df['Gender'] == "Female"]
fe_sum = female["MonthlyIncome (Rs.)"].sum()
# print(female)
# print("all females tot income is: ",fe_sum)

avg_income = df["MonthlyIncome (Rs.)"].mean()
print(avg_income)
df_filter = df[df["MonthlyIncome (Rs.)"] > avg_income]
print(df_filter)




import pandas as pd

df1 = pd.read_csv("workshop1.csv")
df2 = pd.read_csv("workshop2.csv")

print("Workshop 1 Data:\n", df1, "\n")
print("Workshop 2 Data:\n", df2, "\n")

# (a) Find names of students who attended BOTH workshops
both = pd.merge(df1, df2, on="Name", suffixes=("_w1", "_w2"))
print("(a) Students who attended both workshops:\n", both["Name"].tolist(), "\n")

# (b) Find names of students who attended ONLY ONE workshop
# Use outer merge and find where Name appears only once
merged_outer = pd.merge(df1, df2, on="Name", how="outer", indicator=True)
single_only = merged_outer[merged_outer["_merge"] != "both"]["Name"]
print("(b) Students who attended a single workshop only:\n", single_only.tolist(), "\n")

# (c) Merge two data frames row-wise (stack them)
merged_rowwise = pd.concat([df1, df2], axis=0)
print("(c) Row-wise merged DataFrame:\n", merged_rowwise, "\n")
print("Total number of records:", len(merged_rowwise), "\n")

# (d) Merge row-wise again, set Name and Date as multi-row index
#     and generate descriptive statistics
df_hierarchical = merged_rowwise.set_index(["Name", "Date"])
print("(d) Hierarchical DataFrame:\n", df_hierarchical, "\n")

print("Descriptive Statistics for Hierarchical DataFrame:")
print(df_hierarchical.describe())


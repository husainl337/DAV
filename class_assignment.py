import numpy as np
import pandas as  pd
#Q1
df  = pd.read_csv("data.csv")

# print("First 5 rows: \n", df.head())
# print("Shape of the dataframe: \n", df.shape)
# print("Names of columns are: \n", df.columns)

# Q2 
# print("Missing Values: ")
# print(df.isnull().sum())
# df.fillna(df.mean(numeric_only=True), inplace=True)

#Q3
df["Total"] = df["Height"] + df["Weight"]
# print(df.head())

#Q4
# df_sorted = df.sort_values(by="Height", ascending=False)
# print(df_sorted)

#Q5
df_filter = df[df["Weight"] > 80]
# print(df_filter.head())

#Q6
new_df = df.groupby("Type1")
# print(new_df.mean(numeric_only=True))


#Q7
array = np.random.randint(10,100, size=(4,4))
# print("array: \n", array)
# print("first 2 rows of array: \n", array[:2])
# print("all elements is 2nd column: \n", array[:, 1:2])


#Q8
d1 = np.array([10,20,30,40,50])
# print("before swap: \n", d1)
a = d1[0]
d1[0] = d1[-1]
d1[-1] = a
# print("after swap: \n", d1)


#Q9
arr = np.array([[1,0,0],
                [0,1,0],
                [0,0,1]])
# print("before transpose:\n",arr)
# print("after transpose:\n",arr.transpose())

#Q10
arr1 = np.arange(1,11)
# print("array created:\n",arr1)
# print("sliced 3rd to 7th index:\n",arr1[3:8])
arr1[arr1 %2==0] = -1
# print("replaced even no. with -1:\n",arr1)

#Q11
ran_arr = np.random.randint(1,100, size=10)
# print("array:\n",ran_arr)
# print("\nmean: ",np.mean(ran_arr))
# print("median: ",np.median(ran_arr))
# print("std deviation: ",np.std(ran_arr))

# Q12
data = {"Name":['A', 'B', 'C', 'D', 'E','F'], 
        "Class":[1,2,1,2,2,1],
        "Score1": [85,74,83,64,77,90],
        "Score2": [90,86,71,68,62,87],
        "Score3": [88,80,92,73,72,92]}
score = pd.DataFrame(data)
# print("Dataframe:\n",score)
# print(score[["Name","Class"]])
# print(score[score["Class"]==1]["Name"])
# print(score[score["Score3"] < 80])
# print(score["Class"].value_counts().sort_index())
# print(score.sum(axis="columns", numeric_only=True))

def min_max(min,max):
    return max - min
a = min_max( score["Score1"].min(), score["Score1"].max() )
# print("difference btw max and min of 'Score1' column = ", end="")
# print(a)

# Q13
a = pd.Series([6, np.nan, -4, np.nan, 3, 8, np.nan, 5])
# print(a.sort_values(na_position="first"))
# print(a.rank(ascending=False))
# print(a.dropna())

# Q14
df = pd.DataFrame(np.random.randint(1,101,size=(5,4)), 
                   index=['L','M','N','O','P'], 
                   columns=['col1','col2','col3','col4'])
# print(df)

df1 = pd.DataFrame({'id': [1,3,6,7],  'val' : ['a', 'b','c','d']})
df2 = pd.DataFrame( {'id' : [1,2,3,5,6,8], 'val' :['p','q','r','s','t','u']})
df3 = pd.merge(df1, df2, on= 'id', how = 'outer')
print(df3)
print(df3.isnull().sum())
df3.fillna(method='ffill', inplace=True)
print(df3)






# Q15
a = np.array([[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11],
              [12,13,14,15],
              [16,17,18,19],
              [20,21,22,23]])
# print("array:\n",a)

# print("element at (1,3):",a[1,3])
# print("element at (3,1):",a[3,1])
# print("element at (5,0):",a[5,0])
# print("element at (2,3):",a[2,3])

# print("rows at 0,2,4: \n",a[::2, :])
# print("rows at 1,3,5:\n", a[1::2, :])
# print("values greater than 10:\n",a[a > 10])
# print("rows from 1 to 4 index:\n",a[1:5])
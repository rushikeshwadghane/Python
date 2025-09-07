import pandas as pd

def print_fun(d= None):
    print('results print ---------- -- -- >')
    print()
    print()
    print(d)
    print()
    
    
l=  [
    {"ID": 1, "Name": "Alice", "Age": 25, "City": "New York", "Salary": 50000},
    {"ID": 2, "Name": "Bob", "Age": 30, "City": "Los Angeles", "Salary": 60000},
    {"ID": 3, "Name": "Charlie", "Age": 28, "City": "Chicago", "Salary": 55000},
    {"ID": 4, "Name": "David", "Age": 35, "City": "Miami", "Salary": 65000},
    {"ID": 5, "Name": "Eve", "Age": 22, "City": "San Francisco", "Salary": 52000},
    {"ID": 6, "Name": "rr", "Age": 28, "City": "DC", "Salary": 122000}
]

df = pd.DataFrame(l) #creating data frame 

s = pd.Series([1,2,2]) #creating a single column

h = df.head()  # defult it provide first 5 row of df ------>> Returns the first n rows of the DataFrame.

t = df.tail()   # defult it return lasr 5 row of df ------>> Returns the last n rows of the DataFrame

df.info() # Displays concise summary of DataFrame.

# ex --->
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 6 entries, 0 to 5
# Data columns (total 5 columns):
#  #   Column  Non-Null Count  Dtype 
# ---  ------  --------------  ----- 
#  0   ID      6 non-null      int64 
#  1   Name    6 non-null      object
#  2   Age     6 non-null      int64 
#  3   City    6 non-null      object
#  4   Salary  6 non-null      int64 
# dtypes: int64(3), object(2)
# memory usage: 368.0+ bytes


df.describe()  #Generates descriptive statistics of DataFrame.

# ex --->
#              ID        Age         Salary
# count  6.000000   6.000000       6.000000
# mean   3.500000  28.000000   67333.333333
# std    1.870829   4.427189   27332.520313
# min    1.000000  22.000000   50000.000000
# 25%    2.250000  25.750000   52750.000000
# 50%    3.500000  28.000000   57500.000000
# 75%    4.750000  29.500000   63750.000000
# max    6.000000  35.000000  122000.000000

s = df.shape # Returns the shape of the DataFrame (rows, columns). exx  -- (6,5)

sz = df.size  # return the size of the dataframe -- row * col   -- ex  -- 30

cl =  df.columns  # returns cloumn  of df ex ----- Index(['ID', 'Name', 'Age', 'City', 'Salary'], dtype='object')

ind = df.index # Returns the index (row labels) of the DataFrame.  example ------  RangeIndex(start=0, stop=6, step=1)

df2 = df.set_index('Age') # Sets the DataFrame index using an existing column.

df2 =  df2.reset_index()   # Resets the index to default integer index.

print_fun(df2)
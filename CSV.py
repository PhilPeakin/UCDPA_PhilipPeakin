import pandas as pd
import matplotlib.pyplot as plt
#Import a CSV File into a pandas DataFrame
file = pd.read_csv(r"C:\Users\Philip\Desktop\Data Analytics\Amazon CSV\Bestsellers.csv")
print(file)
Genre = file['Genre']
Rating = file['User Rating']
Reviews = file['Reviews']
file.set_index('Author', inplace=True)
#Using Numpy
import numpy as np
Rating_avg_col = np.mean(Rating,0)
print (Rating_avg_col)
Reviews_avg_col = np.mean(Reviews,0)
print (Reviews_avg_col)
#Dictionary & Lists
Titles = ['10-day green smoothie cleanse', '11/22/63', '12 rules for life: an antidote to chaos', '1984 (signet classics)']
Prices = ['8', '22', '15', '6', '12', '11','30']
Price_list = { '10-day green smoothie cleanse':'8','11/22/63':'22','12 rules for life: an antidote to chaos':'15','1984 (signet classics)':'6' }
print(Price_list)
#Looping
for eachReview in Reviews:
    print(eachReview)
count = 10
while count >= 0:
    print(count)
    count = count - 1
print("Blast Off")
#Grouping
print(file.groupby('Year').agg(np.average))
print(file.groupby(['Year','User Rating']).agg({'Price':(np.average, np.sum)}))
file.groupby('Year')['Price'].transform(np.average)
#Most Expensive Book
Moneybook= file.loc[file["Price"] == file["Price"].max()]
print(Moneybook)
#Sorting
print(file.sort_values(["Reviews", "User Rating"]).head(10))
#Indexing
datafile1 = file.set_index('Year')
datafile2 = datafile1.reset_index()
#Missing Values
df1= file.head(30)
MissingValues1 = df1.isnull()
print(MissingValues1)
MissingValues2 = df1.isnull().sum()
print(MissingValues2)
#Functions
print(len(MissingValues2))
#Merging DataFrames
Author_df= pd.DataFrame([{'Author':'JJ Smith','Genre':'Non Fiction'},{'Author':'Stephen King','Genre':'Fiction'},{'Author':'Jordan B. Peterson','Genre':'Non Fiction'},{'Author':'George Orwell','Genre':'Fiction'},{'Author':'National Geographic Kids','Genre':'Non Fiction'},{'Author':'George R. R. Martin','Genre':'Fiction'},{'Author':'Amor Towles','Genre':'Fiction'}])
print(Author_df)
Author_df= Author_df.set_index('Author')
UR_df= pd.DataFrame([{'Author':'James Comey','User Rating':'4.7'},{'Author':'Fredrik Backman','User Rating':'4.6'},{'Author':'Jaycee Dugard','User Rating':'4.6'}])
print(UR_df)
merge = pd.merge(Author_df,UR_df, how='outer',left_index=True,right_index=True)
print(merge)
#Itterows
df = pd.read_csv(r"C:\Users\Philip\Desktop\Data Analytics\Amazon CSV\Bestsellers.csv", header = None)
print(df)
col2 = [x for x in df[2]]
print(col2)
for i, row in df.iterrows():
    print(i, row[0], row[3], row[4], row[5],)
#Slicing, loc, iloc
df4= pd.read_csv(r"C:\Users\Philip\Desktop\Data Analytics\Amazon CSV\Bestsellers.csv")
print(df4.head())
df4.tail(3)
df4.iloc[:10]
df4.iloc[:, 1].head(5)
df4.iloc[1:7, 2]

df4.loc[::40]
df4.loc[[0,1,2],:]

#Visuals

x = ([1,2,3,4,5,6,7,8,9])
y = ([11,12,13,14,15,16,17,18,19,20])
plt.plot(x,y)
plt.show()
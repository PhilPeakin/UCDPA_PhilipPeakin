import pandas as pd
#Web Scraping 2019 - 2020 NBA Stats (Seperate Data from Main Project)
year = '2019'
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'
url = str.format(year)
print(url)
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
print(Rating_avg_col)
Reviews_avg_col = np.mean(Reviews,0)
print(Reviews_avg_col)
#Dictionary & Lists
Titles = ['10-day green smoothie cleanse', '11/22/63', '12 rules for life: an antidote to chaos', '1984 (signet classics)']
Prices = ['8', '22', '15', '6', '12', '11','30']
Price_list = { '10-day green smoothie cleanse':'8','11/22/63':'22','12 rules for life: an antidote to chaos':'15','1984 (signet classics)':'6' }
print(Price_list)
#Looping
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
print(datafile1)
datafile2 = datafile1.reset_index()
#Missing Values
df1= file.head(30)
MissingValues1 = df1.isnull()
print(MissingValues1)
MissingValues2 = df1.isnull().sum()
print(MissingValues2)
#Dropping Duplicates
Duplicates = file.duplicated(['Name'])
print(file['Name'].duplicated().sum())
file.duplicated(['Name'],keep='first')
file.drop_duplicates(subset = ['Name'])
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
print(df4.shape)
df4.iloc[:10]
df4.iloc[:, 1].head(5)
df4.iloc[1:7, 2]
df4.loc[125:]
df4.loc[::40]
df4.loc[[0,1,2],:]

#Visualization
#Matplotlib
#Most Popular Writer
top_list = file.groupby(["Author"])["Name"].count()
top_list = top_list.sort_values(ascending=False)
print(top_list[:10])
tlist = "JeffKinney","GaryChapman","SuzanneCollins","Rick Riordan","APA", "Gallup","Dr.Seuss","Rob Elliott","Eric Carle","Bill O'Reilly"
ylist = "12", "11" ,"11", "11", "10", "9", "9", "8", "7" ,"7"
#import matplotlib.pyplot as plt
#plt.title('Most Popular Writer')
#plt.xlabel('# of Bestsellers')
#plt.ylabel('Writer')
#plt.plot(ylist,tlist,'m.')
#plt.show()

#Using Seaborn to compare Fiction to Non Fiction
#import seaborn as sns
print("Genre:", '\n', file['Genre'].value_counts())
#sns.countplot('Genre', data=file, palette='Set5')
#plt.show()

#Books with Highest Reviews & Ratings
file['Reviews/Rating'] = file['Reviews']/file['User Rating']
print(file.sort_values('Reviews/Rating', ascending=False).head(10))

#Fiction  vs Non Fiction 2013 - 2019
fiction19 = len(file[(file["Year"] == 2019)& (file["Genre"] == "Fiction")])
non_fiction19 = len(file[(file["Year"] == 2019)& (file["Genre"] == "Non Fiction")])
print(fiction19)
print(non_fiction19)
fiction18 = len(file[(file["Year"] == 2018)& (file["Genre"] == "Fiction")])
non_fiction18 = len(file[(file["Year"] == 2018)& (file["Genre"] == "Non Fiction")])
print(fiction18)
print(non_fiction18)
fiction17 = len(file[(file["Year"] == 2017)& (file["Genre"] == "Fiction")])
non_fiction17 = len(file[(file["Year"] == 2017)& (file["Genre"] == "Non Fiction")])
print(fiction17)
print(non_fiction17)
fiction16 = len(file[(file["Year"] == 2016)& (file["Genre"] == "Fiction")])
non_fiction16 = len(file[(file["Year"] == 2016)& (file["Genre"] == "Non Fiction")])
print(fiction16)
print(non_fiction16)
fiction15 = len(file[(file["Year"] == 2015)& (file["Genre"] == "Fiction")])
non_fiction15 = len(file[(file["Year"] == 2015)& (file["Genre"] == "Non Fiction")])
print(fiction15)
print(non_fiction15)
fiction14 = len(file[(file["Year"] == 2014)& (file["Genre"] == "Fiction")])
non_fiction14 = len(file[(file["Year"] == 2014)& (file["Genre"] == "Non Fiction")])
print(fiction14)
print(non_fiction14)
fiction13 = len(file[(file["Year"] == 2013)& (file["Genre"] == "Fiction")])
non_fiction13 = len(file[(file["Year"] == 2013)& (file["Genre"] == "Non Fiction")])
print(fiction13)
print(non_fiction13)
fiction12 = len(file[(file["Year"] == 2012)& (file["Genre"] == "Fiction")])
non_fiction12 = len(file[(file["Year"] == 2012)& (file["Genre"] == "Non Fiction")])
print(fiction12)
print(non_fiction12)
fiction11 = len(file[(file["Year"] == 2011)& (file["Genre"] == "Fiction")])
non_fiction11 = len(file[(file["Year"] == 2011)& (file["Genre"] == "Non Fiction")])
print(fiction11)
print(non_fiction11)
fiction10 = len(file[(file["Year"] == 2010)& (file["Genre"] == "Fiction")])
non_fiction10 = len(file[(file["Year"] == 2010)& (file["Genre"] == "Non Fiction")])
print(fiction10)
print(non_fiction10)
fiction09 = len(file[(file["Year"] == 2009)& (file["Genre"] == "Fiction")])
non_fiction09 = len(file[(file["Year"] == 2009)& (file["Genre"] == "Non Fiction")])
print(fiction09)
print(non_fiction09)
#Free Books with the highest ratings
FreeBooks= file[file['Price']==0].sort_values('User Rating', ascending=False).head(10)
print(FreeBooks)


import pandas as pd

file = pd.read_csv(r"C:\Users\Philip\Desktop\Data Analytics\Amazon CSV\Bestsellers.csv")

print(file)

Genre = file['Genre']

Rating = file['User Rating']

Reviews = file['Reviews']

file.set_index('Author', inplace=True)

import numpy as np

Rating_avg_col = np.mean(Rating,0)
print (Rating_avg_col)
Reviews_avg_col = np.mean(Reviews,0)
print (Reviews_avg_col)

print(file.groupby('Year').agg(np.average))
print(file.groupby(['Year','User Rating']).agg({'Price':(np.average, np.sum)}))
file.groupby('Year')['Price'].transform(np.average)

print(file.sort_values(["Reviews", "User Rating"]).head(10))

file.index

datafile1 = file.set_index('Year')
datafile1.head()
datafile2 = datafile1.reset_index()
datafile2.head()

datafile1.loc[2019,'Name']

datafile2.iloc[:,[1,3]]


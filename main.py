
import pandas as pd

file = pd.read_excel(r"C:/Users/Philip/Desktop/Data Analytics/BestSellers.xlsx")
print(file)
print(file[0:3])

Genre = file['Genre']
print(Genre)
Rating = file['User Rating']
print(Rating)
Reviews = file['Reviews']
print(Reviews)

file.set_index('Author', inplace=True)

import numpy as np

Rating_avg_col = np.mean(Rating,0)
print (Rating_avg_col)
Reviews_avg_col = np.mean(Reviews,0)
print (Reviews_avg_col)

print(file.head(10))
print(file.sort_values(["Reviews", "User Rating"]).head(10))

file.set_index("Name", inplace=True)

print(file.sort_index(axis=1))

file.index

file.set_index("Name", inplace=True)

s_Reviews = sorted(Reviews)

s_Reviews_Reversed = sorted(Reviews, reverse=True)
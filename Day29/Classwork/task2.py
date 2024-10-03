#შექმენით 2 ლისტი. პირველს მე5ე და მე2ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე3ე და მე4ე ადგილას

import pandas as pd

sheet1 = pd.DataFrame([['', 'Variable in 2nd place', '', '', 'Variable in 5th place']], columns=['A', 'B', 'C', 'D', 'E'])
sheet2 = pd.DataFrame([['', '', 'Variable in 3rd place', 'Variable in 4th place', '']], columns=['A', 'B', 'C', 'D', 'E'])

print("Sheet 1:\n", sheet1)
print("\nSheet 2:\n", sheet2)
######### Q1

import pandas as pd

dewPoint = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/DAAG/dewpoint.csv",header=0,index_col=0)
print(dewPoint)

temps = dewPoint[["maxtemp","mintemp"]]
print(temps)

temps2 = temps * 2
print(temps2)

print( temps2.describe() )



# You have been given an Excel file, BeaverData.xlsx.
# This contains a number of observations of beaver body temperature versus time of day,
# as well as other information. The following libraries are required: readxl and ggplot2
# Libraries required: ggplot2, readxl

# install.packages("readxl")
# install.packages("ggplot2") # requires installing rtools 
library(readxl)
library(ggplot2)

getwd()
# copy BeaverData.xlsx to working directory

# 1. Load this file into a dataframe using the read_excel() function. Assign it to a variable named BeaverData.
BeaverData = read_excel("BeaverData.xlsx")

# 2. Print the contents of BeaverData.
BeaverData

# 3. Using ggplot2, create a plot that makes a line of best fit (regression line), as shown in class.
# The x should be time, and the y should be temp (short for temperature).
# Coloration is not required. You should include the data points (either the jitter points, or just regular points).
# The method should be the linear model (“lm” method).
ggplot(BeaverData, aes(x = time, y = temp)) + geom_point() + geom_smooth(method = "lm", se = FALSE)

# 4. Using ggplot2, create a line plot that makes a (very jagged) 
# line connecting observations. As with the prior problem, 
# the x should be time and the y should be temp.
ggplot(BeaverData, aes(x = time, y = temp)) + geom_line()

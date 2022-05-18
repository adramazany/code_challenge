# Load chemTable, if you have not already done so.
# •	Extract the Fe and Al columns into variables feCol and alCol.  Print out the max of both of these variables.
# •	Add feCol and alCol together into a new vector, feAlCol.
# •	Obtain the average of feAlCol and print out the result.

library(plyr)
library(ggplot2)

chemTable <- read.csv("Pottery.csv",
                      sep=",", header=TRUE)

chemTable

feCol = chemTable$Fe
alCol = chemTable$Al
print(max(feCol))
print(max(alCol))

#feAlCol = feCol+alCol
feAlCol = c(feCol,alCol)
feAlCol
print(mean(feAlCol))


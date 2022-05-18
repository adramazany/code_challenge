# Load chemTable, if you have not already done so.  Using ggplot2, make a graph.
# •	Assign x to the Ca column, and y to the Na column.
# •	Plot the data points (non-jittered) on the graph.
# •	Plot a regression line on the graph, using linear regression via the method described in cla

library(plyr)
library(ggplot2)

chemTable <- read.csv("Pottery.csv",sep=",", header=TRUE)
chemTable

ggplot(chemTable, aes(x = Ca, y = Na)) + geom_point() + geom_smooth(method = "lm", se = FALSE)

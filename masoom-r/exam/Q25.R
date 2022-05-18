# Load chemTable, if you have not already done so.
# •	Using the ddply() function, split chemTable up by the Site variable as the independent variable.
# •	Using the summarize() function with ddply, specify four summaries to calculate: sdAl, sdFe, sdCa, sdNa.
# •	Calculate the standard deviation of the Al, Fe, Ca and Na columns in the appropriate summary.  Print out the result.
# NOTE: Everything you do MUST be as part of the ddply() call.

library(plyr)
library(ggplot2)

chemTable <- read.csv("Pottery.csv",sep=",", header=TRUE)
chemTable

ddply(chemTable, .(Site), summarize,
      sdAl= sd(Al), 
      sdFe= sd(Fe), 
      sdCa= sd(Ca), 
      sdNa= sd(Na)) 
      

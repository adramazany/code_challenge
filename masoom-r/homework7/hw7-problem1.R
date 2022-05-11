# This exercise starts with a single data set located in a database. We will extract this data, and
# then save it and load it as a JSON data set and a CSV file. Each time we load it we will print out
# the dataset to make certain the contents are the same.

#install.packages("jsonlite")
#install.packages("RSQLite")
library(jsonlite)
library(RSQLite)

#setwd( "./masoom-r/homework7/" )
getwd()
# copy PlanetData.db to working directory

# 1. You have been given a data set stored in an SQLite database, named PlanetData.DB.
# a. Connect to the database using dbConnect().

con <- dbConnect(RSQLite::SQLite(), "PlanetData.db")
print(con)

# b. List the tables in the database, using dbListTables(), and print out the result. You should see only one table.
print(dbListTables(con))

# c. Load that table using dbReadTable(). The name should be “PlanetMass”. This should return a dataframe. Assign it to a variable named planetSQL.
planetSQL = dbReadTable(con, "PlanetMass")

# d. Disconnect from the database using dbDisconnect().
dbDisconnect(con)

# e. Print the contents of planetSQL.
planetSQL

# 2. Now we want to convert the dataframe to a JSON object.
# a. Use the toJSON() function convert planetSQL into JSON code. Name the variable containing the code outJSON.
outJSON <- toJSON(planetSQL)

# b. Write out outJSON using the writeLines() function, with a filename of “planet.json”.
writeLines(outJSON,con="planet.json")

# c. Use the readLines() function to read the file “planet.json”. Name the variable containing the code incomingJSON.
incomingJSON = readLines("planet.json")

# d. Use the fromJSON() function to parse the JSON code in the incomingJSON variable into a dataframe. Name the dataframe planetJSON.
planetJSON = fromJSON(incomingJSON)

# e. Print out the contents of planetJSON.
planetJSON

# 3. We want to convert the dataframe to a CSV file at this point.
# a. Use the write.table() function to write out the planetJSON dataframe to a file named “planet.csv”.
write.table(planetJSON,"planet.csv")

# b. Use the read_delim() function to read in a datatable (data.table) from the file named “planet.csv”. Store it in a variable named planetDataTable.
planetDataTable = read.delim("planet.csv")

# c. Print out planetDataTable, as well as the class of the variable. Note that it is not a dataframe, but is instead a related class.
planetDataTable
class(planetDataTable)

# d. Use the read.table() function to read “planet.csv” a second time. Store it in a variable named planetCSV.
planetCSV = read.csv("planet.csv")

# e. Print out planetCSV. Note that this one is a dataframe.
planetCSV


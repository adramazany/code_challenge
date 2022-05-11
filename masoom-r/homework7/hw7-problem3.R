# Write a function named getMddle(). It takes in one parameter, a vector.
# The function should take the vector and remove the first and last elements,
# and then return the middle elements in a new vector.
# Error checking is not required (so if you get a vector with one element,
# do not worry if the function malfunctions or there is a crash).
# For instance, if I write the following code:
# testVector <- c(1, 2, 3, 4, 5)
# getMiddle(testVector)
# The result of getMiddle() should be a vector with the values 2, 3 and 4.
# It is recommended that you include this test code at the bottom of your own code for problem 3
# to demonstrate that your function works. It should also adapt to the size of the vector,
# so you should determine the size of the vector before extracting the elements into a new vector.
# The length() function may be of use here. Do not use conventional loops –
# only use the programming capabilities discussed up to chapter 8.
# NOTE: This should be doable in a few lines of code.
getMiddle <- function (v)
  mid = v[3 : length(v)-1]
  return(mid)

testVector <- c(1, 2, 3, 4, 5)
mid=getMiddle(testVector)
mid

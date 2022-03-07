#
cList = list([9, 4, 7, 3, 8])
#
cTuple = (5, 4, 3, 5, 2)
#
productList = list()
#
listLen = len(cList)
#
loopIndex = 0
while(loopIndex<listLen):
    # a,b
    productOfPair = cList[loopIndex] * cTuple[loopIndex]
    # c
    productList.append(productOfPair)
    # d
    loopIndex += 1
#
total = 0
loopIndex = 0
while(loopIndex<listLen):
    #
    total += productList[loopIndex]
    #
    loopIndex += 1
# 5
print(productList)
print(total)
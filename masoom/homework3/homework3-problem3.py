def sumMiddle(dataList):
    # 1
    lengthOfList = len(dataList)
    if(lengthOfList<3):
        return dataList
    # 2
    sliceToSum = dataList[1:lengthOfList-1]
    # 3
    middleSum = sum(sliceToSum)
    # 4
    dataList[1:lengthOfList-1]=[middleSum]

def program():
    # 1
    myList=list([2, 4, 6, 8, 10])
    # 2
    print(myList)
    # 3
    sumMiddle(myList)
    # 4
    print(myList)
    # 5

program()
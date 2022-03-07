def buildMultTable():
    #
    mulTable=list()
    #
    for outerLoop in range(0,9):
        # 1
        innerLoop=0
        # 2
        currentLine = list()
        # 3
        for innerLoop in range(0,9):
            # a,b
            currentLine.append( innerLoop * outerLoop )
        # 4
        mulTable.append(currentLine)
    #
    return mulTable
#
mt = buildMultTable()
#
print(mt)

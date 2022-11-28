# def getFirst(myList):
#     return myList[0]


# print(getFirst([1,2,3,4,5,6,7,8,9,10]))

# def getSum(myList):
#     sum = 0
#     for item in myList:
#         sum = sum + item
#     return sum

# print(getSum([1,2,3,4]))

# def getSum2(myList):
#     sum = 0
#     for row in myList:
#         for item in row:
#             sum += item
#     return sum

# print(getSum2([[1,2,5],[3,4,6]]))


def searchBinary(myLists, item):
    first = 0
    last = len(myLists) -1
    foundFlag = False
    while(first <= last and not foundFlag):
        mid = (first + last) // 2
        if myLists[mid] == item:
            foundFlag = True
        else:
            if item < myLists[mid]:
                last = mid -1
            else:
                first = mid + 1
    
    return foundFlag

result = searchBinary([8,9,10,100,1000,2000,3000],10)
print(result)
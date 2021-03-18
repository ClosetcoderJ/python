simpleString = "문자열"
simpleList = ["리", "스", "트"]
simpleTuple = ("튜", "플")


strToList = list(simpleString)
listToTuple = tuple(simpleList)
tupleToStr = str(simpleTuple)

print("str -> list = ", strToList)
print("list ->tuple = ", listToTuple)
print("tuple -> str = ", tupleToStr)

print(len(simpleString))
print(len(simpleList))
print(len(simpleTuple))

numberTuple = (1, 2, 3)
print(numberTuple[0])

# numberTuple[0] = 4
# print(numberTuple[0])
# 에러뜸

oddTuple = (1, 3, 5, 7, 9)
evenTuple = 2, 4, 6, 8, 10

fullTuple = oddTuple + evenTuple

print(fullTuple)

multiTuple =(1,) # 요소가 하나짜리일땐 (1)이랑 헷갈릴수있어서 콤마붙임)

print(multiTuple * 5)

dashTuple = ("=", ) * 3
asteriskTuple =("*",) * 3
fullTuple = dashTuple + asteriskTuple

print(fullTuple)
num
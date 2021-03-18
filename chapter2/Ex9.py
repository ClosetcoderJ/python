oddRange = range(1, 10, 2)
evenRange = range(2, 10, 2)


print(oddRange)
print(evenRange)
print(list(oddRange))
print(list(evenRange))

tenRange = range(1, 11, 1)
tenRange1 = range(10, 0, -1)

# 1 ~ 10 까지 모든 수를 갖고 있는 Range
range1 = range(1, 11, 1) #range라고 변수명 지으면 안됨
range2 = range(1, 11)

# 10 ~ 1 까지 모든 수를 갖고 있는 Range
range3 = range(10, 0, -1)

print(range1 + range2) #오류뜸




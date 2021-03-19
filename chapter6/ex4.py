print("미세먼지 농도: ", end="")
fineDust = int(input())

if fineDust >= 5:
    print("집에 있는다.")
else:
    print("밖에 나간다.")

print("돈: ", end="")
money = int(input())

if money >= 10000:
    print("택시를 타고간다")
else:
    print("버스를 탄다")

print("비가온다면 1, 그렇지않다면 0")
isRaining = int(input())

if isRaining == 1:
    print("우비를 입는다")
else:
    print("선글라스를 쓴다.")



print("숫자를 입력하세요: ", end="")
number = int(input())
if number%2 == 0:
# print("2 *1 = %d", % 1*2) 이렇게도 가능
    print("2 * 1 = 2")
    print("2 * 2 = 4")
    print("2 * 3 = 6")
    print("2 * 4 = 8")
    print("2 * 5 = 10")
    print("2 * 6 = 12")
    print("2 * 7 = 14")
    print("2 * 8 = 16")
    print("2 * 9 = 18")
else:
    print("3 * 1 = 3")
    print("3 * 2 = 6")
    print("3 * 3 = 9")
    print("3 * 4 = 12")
    print("3 * 5 = 15")
    print("3 * 6 = 18")
    print("3 * 7 = 21")
    print("3 * 8 = 24")
    print("3 * 9 = 27")


# 큰 수 출력하기
print(" 두 수를 입력하세요", end="")
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num1)
else:
    print(num2)

print(" 세 수를 입력하세요", end="")
num1 = int(input())
num2 = int(input())
num3 = int(input())


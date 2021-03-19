'''
if 조건문 : 프로그램의 흐름을 만들 수 있는 첫 단계
특정 조건을 만족할 때 소스코드들을 실행

코드 블록 : 여러 소스 코드를 한 덩어리로 뭉침
일반적인 프로그래밍 언어 - { }
파이썬 - 들여쓰기
'''

if True:
    print("조건식이 참이므로")
    print("소스코드가 실행됩니다.")

if False:
    print("조건식이 거짓이므로")
    print("소스코드가 실행되지 않습니다.")

print("프로그램 종료")

# 개별적으로 실습해보기.
print("오늘의 미세먼지 농도를 입력하세요")

findust = input()
findust = int(findust)

if findust >= 5:
    print("마스크를 쓰세요")

print("보유하고 있는 현금을 입력하세요")
money = input()
money = int(money)
if money >= 10000:
    print("택시를 탄다")

print("비가 오나요? 온다면1, 오지않는다면 0을 입력하세요")

isRaining = input()
isRaining = int(isRaining)
if isRaining == 1:
    print("우비를 입는다.")
    print("나간다.")

print("1~10사이의 수를 입력하세요")
number = input()
number = int(number)
if number % 2 == 1:
    print("홀수")

print("수 :", end="")
numb1 = int(input)
if numb1 % 2 == 1:
    print("홀수")
if numb1 % 2 == 0:
    print("짝수")




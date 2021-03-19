pocket = ['paper', 'cellphone', 'money']

money = 'money' in pocket #true false값 나옴. 안에 있는지 물어보는거.

if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#pocket에 없는것도 물어볼수있다. in연산자로.

pocket = ['paper', 'cellphone']

card = True
money = 'money' in pocket

if money:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

'''
이것과
if money:
    print("택시를 타고 가라")
else: 
    if card:
        print...
'''
# if elif else 예제
print("1.콜라 2.사이다 3.환타")
option =int(input())
if option == 1:
    print("콜라")
elif option == 2:
    print("사이다")
elif option == 3:
    print("환타")
else:
    print("제공하지 않는 메뉴입니다.")

print("x 값 : ", end="")
var = int(input())
print("y 값 : ", end="")
var2 = int(input())

if var > var2:
    print("x가 y보다 큽니다.")
elif var < var2:
    print("x가 y보다 작습니다.")
else:
    print("x와 y가 같습니다.")

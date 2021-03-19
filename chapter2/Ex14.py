# set은 집합과 관련된 type
# 수학에서의 집합 : 1.원소의 순서는 고려사항이 아니다 2.원소는 중복될 수 없음
# 딕셔너리랑 헷갈릴 수 있음
numberSet = {1, 2, 3}

stringSet = {"파", "이", "썬"}
print(numberSet)
print(stringSet)

numberSet = {1, 2, 1, 3}
stringSet = {"파", "이", "이", "썬"}
print(numberSet)
print(stringSet)            # 중복요소는 빠지고 만들어짐
# 인덱스 번호가 없다. 데이터가 유일해서 그럼

#실습
numberSet = {1, 2, 3}
emptySet = {}
print(numberSet)
print(emptySet)

print(type(numberSet))
print(type(emptySet))

#공집합 만들거나 시퀀스객체를 set타입으로 만들고싶을때 씀
#변수명 = set(시퀀스객체)

emptySet = set()
numberSet = set([1, 2, 3])
stringSet = set("파이썬")

print(emptySet)
print(numberSet)
print(stringSet)

print(type(emptySet))
print(type(numberSet))
print(type(stringSet))

# 교집합 :&또는 intersection 기능
leftSet = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
rightSet = set([2, 4, 6, 8, 10, 12, 14, 16, 18])

#교집합
print(leftSet & rightSet)
print(leftSet.intersection(rightSet))

#합집합 | 또는 union
print(leftSet | rightSet)
print(leftSet.union(rightSet))

#차집합 -또는 difference기능
print(leftSet - rightSet)
print(leftSet.difference(rightSet))

                                        # set의 활용 : 논문표절, 과제짜집기 잡아내는것

numberSet = {1, 2, 3}

numberSet.add(4)
numberSet.add(7)
numberSet.remove(7)    #지우는것도 가능
# 리스트, 튜플 : 인덱스를 지정해서 지움
# 셋 : 삭제할 데이터를 직접 지정
leftSet = set("나는 오늘도 파이썬을 공부한다.")
# rightSet = {"나는 내일도 파이썬을 공부한다."}  처음 할때 이렇게함 이렇게할려면 {"나", "는"...}이런식으로 해야됨
rightSet = set("나는 내일도 파이썬을 공부한다.")

print(leftSet | rightSet)
print(leftSet & rightSet)
print(leftSet - rightSet)


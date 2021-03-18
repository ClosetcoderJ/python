"""
 리스트는 요소를 추가 또는 삭제할 수 있다.
 - 요소 추가 : append, insert
 - 요소 삭제 : pop
"""

# 4명의 시험 성적
numberList = [14, 75, 32, 94]

# 전학온 학생의 성적
numberList.append(77) #append는 맨 뒤에 데이터를 저장
print(numberList)

numberList.insert(0, 59) #insert는 삽입하는것(특정 인덱스에 데이터를 저장)
print(numberList)

# 맨 뒤 데이터 제거

deleteNumber = numberList.pop() # input 처럼 값을 반환함(꺼낸다고봐라)
print("삭제한 데이터 =%d" % deleteNumber)
print(numberList)

#특정 인덱스의 데이터를 제거
numberList.pop(0)
print(numberList)

'''
append 메서드 또는 pop 메서드를 인덱스 번호 없이 사용할 때는 조심할 부분이 없음
(리스트의 맨 뒤에 데이터를 추가하거나 삭제하는 동작)
insert 메서드 또는 pop메서드를 인덱스번호 있이 사용하려 할때는 조심해야함
(리스트의 중간 또는 맨 앞에 데이터를 추가하거나 삭제하는 동작) 필기보기
'''
# numberList[4] = 77
# print(numberList)
#
# numberList = numberList + [77]

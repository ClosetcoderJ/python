
text = "python is easy"

# python
print(text[0:6])

# is
print(text[7:9])

# easy
print(text[10:14])

# python
print(text[:6]) #첫번호 생략가능

# easy
print(text[10:]) #끝생략가능


# 인덱스 번호 하나를 지정해서 접근할 때는 인덱스 범위를 벗어나면 안된다.
# ex) print(text[14])
#슬라이싱할때는 범위 벗어나도 괜찬음
print(text[10:15])


text1 = "Life is too short, You need Python"

print(text1[5:7])

print(text1[8:11])

print(text1[19:])

print(text1[:19])

print(text1[:])


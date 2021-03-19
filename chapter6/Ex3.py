print("중간고사 성적 : ", end="")
score = int(input())
print("레포트 점수 : ", end="")
grade = int(input())

if score >= 50:
    if grade >= 5:
        print("Perfect Pass")
    if grade < 5:
        print("Pass")

if score < 50:
    if grade >= 5:
        print("Fail")
    if grade < 5:
        print("Perfect Fail")

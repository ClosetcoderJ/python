# 성적 : 0 ~ 100
score = 50
# 과제 : 0 ~ 10
report = 10

# 성적이 80점 이상이면서 과제 점수가 10점이면 A+
# 성적이 80점 이상이면서 과제 점수가 10점이 아니면 A

# if score >= 80:
#     if report == 10:
#         print("A+")
#
#     if report != 10:
#         print("A")
# 또는 밑으로와 같이 가능
if score >= 80 and report == 10:
    print("A+")

if score >= 80 and report != 10:
    print("A")


print("미세먼지 농도 : ", end="")

finedust = int(input())
if finedust >= 5:
    print("마스크를 쓰고 나간다")
    print("현금 : ", end="")
    money = int(input())

    if money >= 10000:
        print("택시를 탄다")

score
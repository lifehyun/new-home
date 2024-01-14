# if ~ else문 

# x = int(input("양의 정수를 입력하세요:")) 

# if x % 2 == 0:
#     print("짝수이다")
# else :
#     print("홀수이다")


# 자격증 시험 합격/불합격 판정하기
# 합격조건 필기성적 80점 이상 , 실기 성적 80점 이상
pilgi = int(input("필기시험 점수는? "))
silgi = int(input("실기시험 점수는? "))

if pilgi >= 80 and silgi >= 80 :
    result = "합격"
else :
    result = "불합격"

print("-필기시험 점수: %d"% pilgi)
print("-실기시험 점수: %d"% silgi)
print("-합격여부: %s"%result)

# char = input("영어 소문자 하나를 입력하세요:")

# if char == "a" or char == "e" or char == "o" or char == "u" :
#     print("%s 은(는) 모음이다"%char)
# else :
#     print("%s은(는) 자음이다"%char)

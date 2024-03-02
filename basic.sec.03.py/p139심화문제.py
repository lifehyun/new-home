#문제 1
#등급(A+,A , B, D+, D , F)를 입력받아 평점을 계산하는 프로그램을 작성하라
#A+:4.5 A:4.0 , B+:3.5 , B:3.0 ,  C+:2.5 , C:2.0 , D+: 1.5 , D:1.0 , F:0

# rating = input("등급을 입력해 주세요(A+ , A , B+ , B , C+ , C , D+ , D , F ):")

# if rating == "A+":
#     score = 4.5
# elif rating == "A":
#     score = 4.0
# elif rating == "B+":
#     score = 3.5
# elif rating == "B":
#     score = 3.0
# elif rating == "C+":
#     score = 2.5
# elif rating == "C":
#     score = 2.0
# elif rating == "D+":
#     score = 1.5
# elif rating == "D":
#     score = 1.0
# else :
#     score = 0
# print(f"등급:{rating},평점:{score}")   

#문제2
#두시간 중 빠른 시간과 늦은 시간을 찾는 프로그램을 작성하시오.
# time1 = int(input("첫 번째 시간의 시를 입력하세요: "))
# time2 = int(input("첫 번째 시간의 분을 입력하세요: "))
# time3 = int(input("두 번째 시간의 시를 입력하세요: "))
# time4 = int(input("두 번째 시간의 분을 입력하세요: "))


# print(f"-빠른 시간 :{time1}:{time2}")
# print(f"-늦은 시간 :{time3}:{time4}")

#문제3
#일주일간 일한 시간에 따라 주급을 계산하는 프로그램을 작성하시오.
#단 시급은 12,000원 40시간을 초과하는 시간에는 오버타임을 적용하여 시급을 1.5배를 적용하여 계산함.


Name = input("이름은 입력하세요: ")
Work_7 = int(input("일주일간 일한 시간을 입력하세요: "))

TimeMoney = 12000
OverTime = Work_7 - 40
NomalmMoney = 12000 * 4

print(f"이름 : {Name}")
print(f"일주일간 일한 시간 : {Work_7}시간")
print(f"오버타임 : {OverTime}시간")

if Work_7 <= 40:
    print(f"주급 :{NomalmMoney}원")
else :
    print(f"주급:{int(NomalmMoney + TimeMoney * 1.5)}원" )

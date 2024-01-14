# 영문 소문자를 대문자로 변환하는 프로그램을 작성했다.
# a = "apple"
# b = a.upper()
# print(b)

# char = input("영문 대문자 또는 소문자 하나를 입력하세요:")
# char2 = char.upper()

# if char2 == "A" or char2 == "E" or char2 == "I" or char2 == "O" or char2 == "U":
#     print("%s-> 모음"%char)
# else :
#     print("%s-> 자음"%char)

# #다이어트 필요성을 판정하는 프로그램이다
# height = int(input("키는?"))
# weight = int(input("몸무게는?"))

# s = weight - 100 *  0.9

# print("=" * 50)
# print("키:",height)
# print("몸무게:",weight)

# if weight >= s :
#     print("건강을 위해 다이어트가 필요합니다.")
# else :
#     print("표준 또는 마른 체형입니다")

# 아르바이트 급여를 계산하는 프로그램을 작성했다
print("아르바이트 급여 계산 프로그램")
print("※ 시급")
print("-주간 근무 : 9,500원")
print("-야간 근무 : 주간 시급* 1.5")

hour_pay = 9500

a = int(input("1(주간근무)또는 2(야간근무)을 입력해주세요: "))
work_time = int(input("근무시간을 입력해주세요: "))

if a == 1 :
    day_night = "주간"
    pay = hour_pay * work_time 
    print("5시간 동안 일한 주간급여는 %d원 입니다"%pay)
elif a == 2 :
    day_night = "야간"
    pay = hour_pay * work_time * 1.5
    print("5시간 동안 일한 야간급여는 %d원 입니다"%pay)
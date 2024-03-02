# 할인율에 따라 지불 금액을 계산하라.
# spend = int(input("구매 금액은?"))

# if  spend >= 10000 and spend < 50000 :
#     rate = 5.0
# elif spend >= 50000 and spend < 300000:
#     rate = 7.5
# elif spend >= 300000 :
#     rate = 10.0
# else :
#     rate = 0

# discount = spend * rate / 100 #할인금액 계산
# pay = spend - discount #지불금액 계산

# print("구매금액:%.0f"%spend)
# print("할인율:%.1f"%rate)
# print("할인금액:%.0f"%discount)
# print("지불금액:%.0f"%pay)


# 서비스 만족도에 따라 팁을 계산하는 프로그램이다.
# print("서비스 만족도")
# print("1:매우만족")
# print("2:만족")
# print("3:불만족")
# a = input("서비스 만족도는?(1/2/3)")
# price = int(input("음식 값은?"))

# if a == "1" :
#     tip = int(price*0.2)
#     service = "매우 만족"
# elif a == "2" :
#     tip = int(price*0.1)
#     service = "만족"
# else :
#     tip = 0
#     service = "불만족"    
# print()
# print("서비스 만족도:%s,팁:%d원"%(service,tip))


# 세 정수중 가장 큰 수를 찾는 프로그램이다.
# num1 = int(input("첫번째 정수는?"))
# num2 = int(input("두번째 정수는?"))
# num3 = int(input("세번째 정수는?"))

# if num1 > num2  and num1 > num3 :
#     largest = num1
# elif num2 > num3 and num2 > num1 :
#     largest = num2
# else :
#     largest = num3

# print("%d, %d, %d 중에서 가장 큰수는 %d 입니다."%(num1,num2,num3,largest)) 

#웹 사이트 콘텐츠 이용 가능 여부를 판단하는 프로그램입니다.
# userid = input("아이디는?")

# if userid == "admin" :
#     print("콘텐츠 이용이 가능합니다.")
# else :
#     level = int(input("회원 레벨은?(1-9)"))

# if  level >= 1 and  level <= 3 :
#     print("콘텐츠 이용이 가능합니다!")
# else :
#     print("콘텐츠를 이용할 수 없습니다!")

#온도에 따라 물의 상태를 판별하는 프로그램입니다.
unit = input("단위를 입력해주세요(1:섭씨,2:화씨)")
temp = int(input("온도를 입력해주세요 :"))

if unit == "2":
    temp =(temp - 32)*5/9

if temp <= 0:
    state = "고체"
elif  temp < 100 :
    state = "액체"
else :
    state = "기체"

print("물의 섭씨 온도:%.1f도 상태:%s"%(temp,state))
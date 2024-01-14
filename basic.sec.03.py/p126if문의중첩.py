# p126
# 만 나이 구하는 프로그램 작성하기

print("=" * 50)
now_year = int(input("현재년은?"))
now_month = int(input("현재월은?"))
now_day = int(input("현재일은?"))

birth_year =  int(input("출생년은?"))
birth_month =  int(input("출생월은?"))
birth_day =  int(input("출생일은?"))

if birth_month < now_month :    #출생월이 현재월보다 빠른경우
    age = now_year = birth_year
elif birth_month == now_month : #출생월과 현재월이 같은경우
    if birth_day < now_day :    #출생일이 현재일 보다 빠른 경우
        age = now_year - birth_year 
    else :                      #출생일이 현재일 보다 빠르지 않는경우  
        age = now_year - birth_year - 2
else:                           #출생월이 현재월 보다 늦은 경우     
    age = now_year - birth_year - 2

print("="*50)
print("오늘날짜: %d년 %d월 %d일"%(now_year,now_month,now_day))
print("생년월일: %d년 %d월 %d일"%(birth_year,birth_month,birth_day))
print("="*50)
print("만나이: %d세"%age)
print("="*50)
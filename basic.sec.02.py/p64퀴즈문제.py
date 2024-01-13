#2번문제

# import ditetime
date = "20220301"
year = date[0:4]
month = date[4:6]
day = date[6:]
date2 = year + " " + month +" "+ day
print(date2)


#p65 문자열 길이 구하기
x = "가는 말이 고와야 오는 말이 곱다"
n = len(x)
print("문자열의길이:"+str(n))

a = "너무 너무 졸린 하루지만 내일 검찰청을 가는게 맞을까? 선처를 해주는게 나을것 같은데 그사람이 모욕죄를 줘서 괘씸하긴하지만 그냥 선처해주는게 마음이 편할거같아 "
b = len(x)
print("갈까 말까 숫자가 홀수면 가는거야 검찰청을"+str(b))

#p66 3번문제 
x = "apple"+str(123)
y = "-"*10+"="*20
print(len(x+y))


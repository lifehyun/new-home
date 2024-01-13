#변수의 타입을 알아보는 함수 type

# 삼성전자라는 변수로 50,000원을 바인딩해보세요.
# 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsung = 50000
samg = 10
avg = samsung*samg
print(avg)
print("-----------------")
#삼성전자의 일부 투자정보입니다.
# 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
siga = 298
hun = 50000
per = 15.79
print(f"시가총액 {siga}조")
print(f"현재가 {hun}원")
print(f"PER {per}")
print("-----------------")
s = "hello"
t = "python"
print(s+"!",t)
print("-----------------")
#출력예상값 8
a = 2+2*3
print(a)
print("-----------------")
#type 함수 변수 a 128
a = 128
b = 132
print (type(a))
print(type(b))
#문자열"720"을 정수형으로 변환해보세요.
num_str = "720"
print(type(num_str))
num_int = int(num_str)
print(type(num_int))
print("-----------------")
#정수 100을 문자열"100"으로 변환해보세요
nu = 100
nust = str(nu)
print(type(nust))
print(nust)
print(type(nu))
print(nu)
print(type(nust))
print("-----------------")

#문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
mon = "15.79"
f = float(mon)
print(mon,type(f))

#year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 
#이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요. 
year = "2020"
y = int(year)
print(y-1); print(y-2); print(y-3)

#에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매
#총 금액은 계산한 후 이를 화면에 출력해보세요.
air = 48584
mo =  36
avg = air * mo
print(f"총판매금액은:{avg}") 



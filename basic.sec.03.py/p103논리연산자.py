# p103 논리연산자

# and 조건1 과 조건2 가 둘다 참인경우에만 참
score1 = 75
score2 = 90
sc = score1 >= 80 and score2 >= 80  #거짓 : False
print(sc)

# 조건3 과 조건4 가 둘다 참이라서 
score3 = 85
score4 = 95
sc1 = score3 >= 80 and score4 >= 80 #참 : true
print(sc1)

# or 조건1 또는 조건2 중 하나만 참이어도 참이된다 
x = 10
x1 = x % 2 == 0 or x % 6 == 0
print(x1)

x2 = 16
x3 = x2 % 3 == 0 or x2 % 5 == 0
print(x3) 

# not 논리부정 조건이 참이면 거짓 거짓이면 참으로 해서 논리 값을 반대로 변경한다.
x4 = 25
x5 = not x4 % 2 == 0
x6 = not x4 > 10
print(x5)
print(x6)
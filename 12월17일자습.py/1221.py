string1 ='l am a genius!'
for i in range(0,14):
    print(f"'{string1[i]}'",end=",")

fruits = ["사과","오렌지","딸기","수박","멜론"]
for i in range(len(fruits)):
   print(f"%d. %s"%(i+1,fruits[i]))

#for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.

for i in range(0,100):
   print(i)

#월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.

for word in range(2002,2051,4):
   print(f"월드컵은 {word}년에  개최된다")
     

# 1부터 30까지의 숫자 중 3의 배수를 출력하라. 
for three in range(3,31,3):
    print(three)
   

# 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
for x in range(99,0,-1):
   print(x)



#1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
sm = 0 
for i in range(1,11):
   sm += i
print(f"합:",sm)


#1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
sum1 = 0
for i in range(1,11,2):
    sum1 += i
print(f"합:",sum1)


#1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
gob = 1
for g in range(1,11):
    gob *= g  
print(gob) 

#아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
for i in range(0,4):
    print(price_list[i])

#len() 함수를 사용하면 price_list 가 변해도 코드의 수정이 필요없습니다. 아래가 더 좋은 코드입니다.
for i in range(len(price_list)):
    print(price_list[i])    

#my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
my_list2 = ["가", "나", "다", "라","마"]
print(my_list[0] ,my_list[1])
print(my_list[1] ,my_list[2])
print(my_list[2] ,my_list[3])

for i in [0,1,2,3] :
    print(my_list)

for i in range(2,len(my_list2)):
    print(my_list2[i-2],my_list2[i-1],my_list2[i-5])   

for i in range(1,len(my_list)):
    print(my_list[i-1],my_list[i-2])

for k in range(10):
    print(k , end=" ")
print("'1번째'") #줄 바꿈

for j in range(8):
    print(j , end=" ")
print("'2번째'") #줄 바꿈

for k in range(1,11):
    print(k , end=" ")
print("'3번째'")

for j in range(1,11 ,2): #1 ~ 10까지 1 , 3 , 5 , 7 , 9이 출력 될것이라고 예상
    print(j,end=" ")
print("'4번째'")

print()
for j in range(2,11,2):
    print(j,sep=" ")
print("'5번째'")



year = 2024
month = 3
day = 2
print(year , end="/")
print(month , end="/")
print(day , end="/")


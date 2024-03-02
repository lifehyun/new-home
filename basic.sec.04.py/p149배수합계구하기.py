#5의 배수 합계 구하기
# sum = 0
# for i in range(100 , 201 ,5):
#     sum += i
#     print("5의 배수의 합계:%d"%(sum))

#if문을 사용하여 5의 배수 구하기
sum = 0

for i in range(100,201): #i의 값: 100~200까지의 속해있다. 
    if i%5 == 0:
        sum += i
    print("5의 배수의 합계 :%d"%(sum))

print(i.__index__())
print(sum.__index__())



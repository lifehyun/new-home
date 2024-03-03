#객체지향 잘 활용하기
import numpy as np
a = np.array([4,5,0,1,2,3,6,7,8,9,10,11]) # numpy에 array 배열을 만들어주는 함수이다.
print(a)
print(type(a)) # 타입을 보는 함수
print(a.shape) #모양을 보는 함수
a.sort() #정렬해주는 함수
print(a)

b = np.array([-4.3, -2.3 , 12.9 , 8.99 , 10.1 , -1.2 ]) #6개가 들어간 배열이다.
print(b)
print(type(b)) # 타입을 보는 함수
print(b.shape) #모양을 보는 함수
b.sort() #정렬해주는 함수
print(b)

c = np.array(["one","two","three","four","five","six","seven"])#7개가 들어간 배열이다.
print(c)
print(c.shape)
print(type(c))
c.sort()
print(c)
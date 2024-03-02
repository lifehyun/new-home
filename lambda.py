#람다식으로 간단하게 예제를 풀어보아요
#lambda란 매개변수 : 표현식

# 합을 더하는 함수를 만들어볼것입니다.
# 원래 표현식
def hap(x,y):
    return x + y

print(hap(1,2))


# 람다 형식으로 표현법
# lambda 매개변수: 결과 리터값 그것을 변수에 담아주면된다.
x1 = (lambda x,y: x + y)(10, 20)
print(x1)
#1번문제
#200~ 800까지의 정수 중에서 5의 배수가 아닌 수를 한줄에 10개씩 출력하는 프로그램이다.
# count = 0
# for i in range(200,800):
#     if i%5 != 0:
#         print("%d"% i,end=" ")
#         count += 1
#         if count%10 == 0:
#             print()

#2번문제 길이환산표
#1~100cm , 1씩증가를 밀리미터(mm) ,미터(m) , 인치(inch)로 환산하는 표를 만드는 프로그램이다.
# print("-"*40)
# print("cm mm m inch")
# print("-"*40)

# cm = 0
# for i in range(1,101):
#     cm += 1
#     mm = int(cm * 10.0)
#     m = float(cm * 0.01)
#     inch = float(cm * 0.3937)
#     print("%d %d %.2f %.1f"%(i, mm, m , inch),sep="" )
# print("-"*40)
# print(cm)
# print(m)
# print(mm)
# print(inch)


# #3번 문제 별표 트리를 만들어라
# for i in range(1,11):
#     i = '*' * i
#     print(i,sep=" ")
#     print()


#응용 
# for i in range(1,5):
#     i = "♥" * i
#     print(i , sep= " ")
#     print()

#더 쉽게 하는방법
# print("*")
# print("* *")
# print("* * *")
# print("* * * *")
# print("* * * * *")
# print("* * * * * *")
# print("* * * * * * *")
# print("* * * * * * * *")
# print("* * * * * * * * *")

#4번 트리모양을 변경하라
# for i in range(10,0,-1):
#     i = "*" * i
#     print(i ,sep=" ")
#     print()

# for i in reversed(range(10)):
#     print('*' * (i + 1))

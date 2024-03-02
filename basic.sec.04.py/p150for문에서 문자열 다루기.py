# word = input("영어 문장을 입력하세요: ")

# for x in word:
#     print(x,end=",")
#     print(word)

# love = input("사랑은 무엇이라고 생각해?")

# for i in love:
#     print(i , end=" ♥ ")


#전화번호에서 하이픈(-) 삭제하기
phone = input("하이픈(-)을 포함한 휴대폰 번호를 입력하세요:")
for p in phone:
    if p != "-":
        print("%s"% p,end=" ")
    print(p)


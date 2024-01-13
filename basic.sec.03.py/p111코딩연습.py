# start = int(input("시작 수는?"))
# end = int(input("끝 수는?"))
# num = int(input("정수를 입력하세요"))

# result = "%d은(는) %d~%d 사이에 없다."% (num,start,end) 

# if num > start  and  num > 77:
#     result = "%d은(는) %d~%d 사이에 있다."% (num,start,end)

# print(result)

# 월을 입력받아 계절을 판별하라
# month = input("월을 숫자로 입력하세요:")

# if month == "3" or month == "4" or month == "5":
#     print("%s월은 봄입니다"% month)
# if month == "6" or month == "7" or month == "8":
#     print("%s월은 여름입니다"% month)
# if month == "9" or month == "10" or month == "11":
#     print("%s월은 가을입니다"% month)
# if month == "12" or month == "1" or month == "2":
#     print("%s월은 겨울입니다"% month)

# 주민번호로 남/여를 판정하는 프로그램입니다.
a = int(input("주민번호 뒷자리 첫번째 숫자를 입력해 주세요:"))

if a == 1 or a == 3:
    print("남성입니다")
if a == 2 or a == 4:
    print("여성입니다")

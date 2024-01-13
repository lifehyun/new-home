
# 원의 둘레와 면적을 구하는 프로그램이다.
# r = float(input("반지름을 입력하세요: "))
# length = 2 * r  * 3.14
# area = r * r * 3.14
# print("반지름:%.2f cm"%r)
# print("원의둘레:%.2f cm"%length)
# print("원의면적:%.2f cm2"%area)

#p89
#인치를 센티미터로 환산하는 프로그램이다
# inch = float(input("인치는?"))
# cm = inch * 2.54
# print(f"{cm} cm")

#p90 
#온라인 서점의 책결제 금액을 계산하는 프로그램이다.
price = int(input("책 값은?"))
discount = int(input("할인율은?"))
delivery = int(input("배송료는?"))

pay = price - (price * (discount/100)) + delivery

print("책 값:%d원"%price)
print("할인율:%d"%discount)
print("배송료:%d원"%delivery)
print("결제금액:%d원"%pay)


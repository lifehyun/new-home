#s2-1 입력받은 킬로그램(kg)을 파운드(pound)와 온스(ounce)로 환신하는 프로그램을 작성하시오
# kg = int(input("변환할 킬로그램(kg)은?"))
# pound = float(kg * 2.204623) 
# ounce = float(kg * 35.273962)

# print("킬로그램",kg)
# print("파운드%.2f"%pound)
# print("온스%.2f"%ounce)

#s2-2 하이픈(-)이 포함된 휴대폰 번호를 입력받아 하이픈이 삭제된 번호를 풀력하는 프로그램을 작성하시오.
pn = input("하이픈(-)이 포함된 11자리의 휴대폰 번호는?")
pn2 = pn.replace("-","")
print("- 입력된 휴대폰 번호:",pn)
print("- 하이픈 삭제된 휴대폰 번호:",pn2)
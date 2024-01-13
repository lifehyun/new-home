#연원일 사이에 :를 삽입해라
year = input("년은?") #2021
month = input("월은?") #2월
day = input("일은?") #5일
print(year,month,day,sep=":")

#사각형의 둘레와 면적을 계산하라
width = int(input("사각형의 너비는?"))
height = int(input("사각형의 높이는?"))
length  = 2*width+2* height  
area = width * height
print("사각형의너비:%dcm"%width)
print("사각형의높이:%dcm"%height)
print("둘레 길이:%dcm"%length)
print("면적:%dcm2:"%area)



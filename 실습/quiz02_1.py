""" #수를 입력받음
while True:
    num = input("수를 입력하세요.")

    if num.isdigit():
        break
    print("정수가 아닙니다. 다시 입력하세요.")

total = 0
to=int(num)

for i in range(1,to+1):
    if i%3==0:
        total += i

print("1부터 {}까지 3의 배수의 합={}".format(to,total))
 """

while True:
    num=input("수를 입력하세요.")#문자형으로 입력받는다.
    if num.isdigit():
        print("num:",num)
        break
    else:
        print("정수가 아닙니다. 다시 입력하세요")

total=0
for i in range(0,int(num),3):#문자형으로 받아서 int형으로 형변환시켜준다. 
    total+=i
    # print("total:",total)
else:
    print("total:",total)

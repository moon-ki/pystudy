#range: 순차적 정수를 만들어내는 함수
#값이 1개 있을 경우= end:0~end 미만의 순차적 정수 리턴
seq = range(10)#10이 end가 되고 시작값은 기본값인 0, 증가값은 기본값인 1이된다.
#seq = range(0,10,1)#같은 의미의 구문
print(seq, type(seq))

#순차 자료형 이기 때문에
print(len(seq)) #길이
print(seq[5])   #indexing
print(seq[3:7]) #slicing 

for i in seq : 
    print(i,end=" ")#for 이용한 순환도 가능함.
else:
    print()    

#거꾸로 가려면 step값을 음수로 주면됨
for i in range(10,0,-2):
    print(i,end=" ")
else:
    print()

#enumerate 함수
print("-------enumerate")
colors=["red","blue","green","yello"]
for color in colors:
    print(color)

i=0
for color in colors:
    print("{0}번 색상은 {1}".format(i,color))
    i+=1

#print(enumerate(colors))
for i, color in enumerate(colors):
    #print(color)
    print("{0}번 색상은 {1}".format(i,color))

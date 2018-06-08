#튜플
#   시퀀스형, 변경불가 자료형

#튜플생성: ()
t=(1,2,3)
print(t,type(t))

#()를 생략해도 튜플로 인식한다.
t=1,2,"Python"
print(t,type(t))

#연결: +
t2 = t+(3,4,5)
print(t2,type(t2))

#반복
print(t*3)

#인덱싱과 슬라이싱 가능: t2에서 Python, 3,4를 추출해보자
print(t2[2:5])

#길이
print("len: ",len(t2))

print("-----------------------")

#Packing, Unpacking
print("t2:",t2)

a,b,c,d,e,f = t2
print("Unpacking:",a,b,c,d,e,f)

#튜블의 요소보다 변수의 수가 적을 때, 에러발생
#a,b,=t2 #too many values to unpack (expected 2) 

#받는 변수의 값이 적더라도 변수 앞에 *을 붙이면 여러 value를 받을 수 이씅ㅁ
a,*b=t2
print(a,b)

#다른 예제 *붙인 변수는 list형임
a,b,*c,d,f = t2
print(a,b,c,d,f)



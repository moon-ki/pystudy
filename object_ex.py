#id: 객체의 주소를 반환하는 메서드
print("id(3):",id(3))

#변수에 3을 담는다.
#3객체를 만들고, 변수에 3객체의 id를 연결해서 심볼 테이블에 저장한다는 것이다.

a=3
#a의 id값을 확인해보자
print("id(a=3):",id(a))

b=3
print("id(b=3):",id(b))
b=4
print("id(b=4):",id(b))

#객체의 심볼 테이블
g_a = 2018
g_b = "symol"

#글로벌 영역
def f(): #로컬 영역 변수확인을 위한 확인
    l_a = "local"
    l_b = 5
    print(locals())#로컬 스코프의 심볼 테이블
print("-----------------: Local")
f()
print("-----------------: Global")
print(globals())#글로벌 변수의 확인 dictionary타입으로 넘어옴

print("f" in globals().keys()) #f라는 객체가 있는지 확인

#객체복사
print("----------object복사")
x=[1,2,3]
#레퍼런스 복사
y=x
print(x==y)
print(hex(id(x)),hex(id(y))) #메모리 주소값이 같다.
x[1]=4
print(y[1])

#복제의 시도:1
y=x[:]      #슬라이싱을 이용한 복제
print("x:",x)
print("y:",y)
x[1]=0
print("x:",x)
print("y:",y)   #y의 값은 손상되지 않음.
print(y[1])

#복재이 시도: copy모듈의 활용
import copy

y=copy.copy(x)
print(x is y) #'=='으로 해도 됨: False 가 됨은 메모리 주소값이 다르기 때문이다.
print("x:",x)
print("y:",y)
x[1]=100
print("x:",x)
print("y:",y)

#깊은 복제
print("----------deep copy")
a=[1,2,3]
b=[4,5,a]
x=[a,b,100]
print("a:",a)
print("b:",b)
print("x:",x)

y = copy.copy(x)
print("y:",y)

a[1]=0
print("a:",a)
print("b:",b)
print("x:",x)
print("y:",y)

#deep copy 시도
y = copy.deepcopy(x)
print("a:",a)
print("b:",b)
print("x:",x)
print("y:",y)
a[1]=100
print("x:",x)
print("y:",y) #완전히 복사되었다.

#deep copy는 객체를 다룰 때, 아주 중요하다.


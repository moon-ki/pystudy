#함수에 관한 코드들

def dummy():
    pass    #구현은 나중에

def printHello():
    print("Hello", "Python")

def times(a,b):
    return a*b

def do_nothing():
    return

#함수의 호출
dummy()
printHello()
print(times(10,10))
print(do_nothing())

def swap(a,b):
    return b,a

s = swap(3,4)
print("s:",s)
s1,s2 = swap(3,4)#자동으로 unpacking함!
print("s1:",s1,"s2:",s2)

print("----------- args")
def func1(t):   #가정상 t로 list가 넘어온다고 기대함
    t[0]*=2

a=[1,2,3]   #list는 변경가능한 객체이다.
func1(a)
print("a:",a)

#immutable 객체를 넘겼을 때, 에러가 발생
#func1((1,2,3))   #TypeError: 'tuple' object does not support item assignment

#func1함수의 매개변수 t가 list 일 경우에만 타도록 변경
def func2(t):
    if isinstance(t,list):
        t[0] *=2
        return True
    else:
        return False

result = func2(a)
print(result,a)

result = func2((1,2,3))
print(result)

#함수 인수는 필요한 개수만큼 만들 수 있다.
#기본값을 미리 선언해 줄 수 있다.
def incr(a,step=1): #두번째 인자값을 넘겨주지 않으면 1이 기본값으로 사용된다.
    return a+step
a=10
print(incr(a))
print(incr(a,3))

#가변인수
#정해지지 않은 개수의 인수값을 받아 사용할 때: *
def get_total(*arg):
    total=0
    for num in arg:
        total+=num
    return total

print("total:",get_total(1,2,3,4,5,6,7,8,9))

#사전 키워드 전달: **
def f(a,b,*args, **kwd):
    print(a,b)
    print(args)
    print(kwd)
print("---------사전키워드")
print(f(10,20))         #a,b전달
print(f(10,20,30,40))   #a,b,args
print(f(10,20,30,40,option1=1, option2=2))

#함수도 객체다
def pulus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print(pulus(10,20))
print(minus(30,40))

def apply(a,b,*funcs):
    for func in funcs:
        #if isinstance (func,function):
        print(func.__name__,func(a,b))
apply(1,2,pulus,minus)

#익명 함수(lambda)
def apply2(a,b,func=pulus):
    return func(a,b)

print("apply2(2,3): ",apply2(2,3))
print("apply2(2,3,multiply): ",apply2(2,3,multiply))
print(apply2(2,3,lambda a,b:a+b))
print(apply2(2,3,lambda a,b:2*a+b))

#람다를 이용한 정렬
#리스트 등 시퀀스 자료형 정렬할 때 key
strings = ["Hello","World","Python","Java"]
strings.sort
print(strings)
strings.sort(key=lambda x:len(x))
print(strings)
#from...import
#특정 모듈에서 지정된 이름값을 불러올 수 ㅣ있음
import mymod
from math import pi, sin, cos,tan 
from mymod import pi, add, subtract, multyply

#모듈명 지정 없이 이름으로만 호출 할 수 있게 됨
print(pi)   #mymod의 pi 으로 가져온다.
#print()

print(add(10,20))

#객체 내부의 __module__을 확인하면 그 객체가 어느 모듈에 속해 있는지 확인가능
#add메서드의 모듈은 무엇일까?
#print(add.__module__)
#print(dir(add.__module__))#add메서드 객체의 내부 변수와 객체의 목록 출력

#add겍체의 모듈에 있는 substract 함수를 실행해 봅시다
#eval: 문자열로 넘겨받은 내용에 대해 실행을 시도
print(eval(add.__module__+".subtract(10,10)"))
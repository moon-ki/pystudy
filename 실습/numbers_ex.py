#수치형 연습

#정수형: int(10진, 2진, 8진, 16진 정수를 표현)
a=2018
type(a)#형식 점검

b=0b1101 #2진수
c=0o23   #8진수
d=0xFF   #16진수

print(a,b,c,d)

#정수형을 2진, 8진, 16진 문자열로 반환
print(bin(a),oct(a),hex(a))

#실수형
print("==========float=========")
a=1.2345
type(a) #형식점검
#a는 float인가?
print(isinstance(a,float))
#a의 값이 정수형태인가?(소수점 없나?)
print(a.is_integer())
a=2.0
print(type(a))
print(a.is_integer())

print("==========complex=========")
#복수형
#실수부+허수부j
cpx = 4+5j
cpx = complex(4,5)
print(cpx,type(cpx))
print(isinstance(cpx,complex))

#실수부와 허수부를 따로 얻을 수 있습니다.: .real, .imag
print(cpx,"real: ",cpx.real) #실수부
print(cpx,"imag: ",cpx.imag) #허수부

#켤레 복소수를 얻을 수 있습니다.: .conjugate()
print(cpx,"켤레: ",cpx.conjugate())

#내장 수치 함수
print("==========수치함수=========")
#절대값(abs)
print(abs(5), abs(-5))
#정수로 변환: int
print(int(3.14159), int("123456"))
#print(int("Python")) #정수형태가 아닌, 문자열을 정수변환할 때, 에러가 발생한다.

#실수로 변환
#print(float(3),float(3.14159),float("Python.0")) #문자를 float로 변환할 수 없다.


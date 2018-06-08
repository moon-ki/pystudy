#print 함수안에 출력할 내용을 인자값으로 전달
print(2018)
print(3.1415)
print("Hello Python")

#여러 내용의 연속 출력: , 로 연결
print("Hello","Python")

#문자열을 합쳐 출력할 때: +로 연결
print("Hello"," ","Python")

#문자열 반복 출력:
print("Python"*3)
print()

#문자열과 다른 형식을 +했을 경우: TypeError
#print(3+"Python")

#Solution: 형변환을 시도한다.
print(str(3)+"Python")

#sep, end 변경
print("남승균","강의중",sep=":",end="\n") # ,로구분, 개행함
print("추가문자열")


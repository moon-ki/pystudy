#문자열 서식

#서식문자
'''
%s: 문자열
%d: 정수
%f: 부동소수
%%: %리터럴
'''
format="I have %d apples" % 10
print(format)
print("interest Rate is %.2f%%" % 1.24)

#두개 이상의 값을 넣고 싶을 때
format = "total: %d개, %d개"
print(format % (10,3))
#format과 값의 형식이 일치하지 않으면 TypeError 발생

#고급포매팅
format_str = "I have {} apples, and I ate {} apples."
print(format_str.format(5,"세개"))

#서식에 설정된 공간의 개수와 실제 값의 개수적으면 indexError 발생
print(format_str.format(10,3,1))
#print(format_str.format(10) #SyntaxError: unexpected EOF while parsing

#이름 기반의 포멧
format_str = "I have {total} apples, and I ate {num} apples."
print(format_str.format(total=10, num=2))
#print(format_str.format(total=10))      #KeyError: 'num'

#dict 객체를 이용한 포맷
print(format_str.format_map({"total":5,"num":99}))
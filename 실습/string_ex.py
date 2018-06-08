#문자형
#   시퀀스형
#   변경불가(immutable) 자료형입니다.
str1 = "Life is too short, you need Python"
str2 = "Welcom Python"

#타입판별
print(type(str1), type(str2))
#instance 판별
print(str1, "str?:",isinstance(str1,str))
#여러줄 문자열
mutiline="""
Java
Python
Linux
"""
print(mutiline)

#문자열 ", ' 사용가능
#print("I said "Yes" ") 문자열 안에 " 들어가도록 하려면..

#Solution 1:
print('I said "Yes"')
#Solution2: 
print("I said \"Yes\"")
print("-------문자열의 인덱싱, 슬라이싱, len------")
#문자열의 인덱싱, 슬라이싱, len
print(str1)
print("print(len(str1)):",len(str1))    #길이: len
print("str1[5]:",str1[7])      #인덱스로 접근가능
print("str1[5:7]:",str1[7:9])    #슬라이싱
print("str1[5:]:",str1[7:])
print("str1[:6]:",str1[:9])
print("str1[:]:",str1[:])
#str1[0]='l'# 변경불가 객체이기 때문에 변경불가

#대소문자 관련
#   upper(): 전체대문자
#   lower(): 전체 소문자
#   swapcase(): 대소문자 전환
#   capitalize(): 첫문자를 대문자
#   title(): 각 단어의 첫글자를 대분자

str3 = str1.lower().title() #매서드 연결
print(str3)
print("-------검색관련------")
#검색관련
print('str1.count("short"):',str1.count("short"))
print('str1.find("Python"):', str1.find("Python"))
print('str1.find("Life",6):',str1.find("Life",6))
print('str1.rfind("Life"):',str1.rfind("Life"))
print('str1.find("Java"):',str1.find("Java"))
#find()는 찾는 내용이 없으면 -1을 반환

print('str1.index("Python"):',str1.index("Python"))
#print('str1.index("Java"):',str1.index("Java"))
#index()는 찾는 내용이 없으면 에러발생!

#분리와 결합
print("-----분리와 결합-----")
s = "Java and Python"
#\해줘야 개행 일어나지 않음
lines = """\ 
Java
Python
Linux
Oracle"""
#분리: split - ' '문자를 기준으로 분리
print("s:",s)
print('s.split():',s.split())        #공백문자 기준 분리
print('s.split(" and "):',s.split(" and ")) #특정 문자열 기준 분리
#합치기: join()
t = s.split(" and ")
# : 문자를 넣어서 합쳐보자
print('":".join(t):',":".join(t))
s2 = "abc:def:ghi:jkl"
#기준 분리한 후, 2개만 가져오기
print(s2.split(":",2))
print(s2.rsplit(":",2))
#splitlines(): 개행 문자를 기준으로 분리
print(lines.splitlines())

#판별 관련
#   isdigit(): 형태가 숫자형태인가
#   isalpha(): 알파벳 형태인가
#   islower(): 소문자 형태인가
#   isupper(): 대분자 형태인가
#   isspace(): 공백문자 형태인가

num = input("정수를 입력하세요: ")#input매서드는 문자열을 입력받기 때문에
result = num*2 #2번 문자열이 반복되어 초기화된다.
print("result:",result)

#Solution 1:
#result = int(num)*2 #int로 형변환
print("result:",result)
#Solution2:
if num.isdigit():
    result = int(num)*2
else:
    result = "정수가 아닙니다."
    
print("result:",result)
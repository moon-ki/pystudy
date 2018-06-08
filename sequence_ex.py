#문자열
print("-------------------------")
#연결: + 
print("Py"+"thon")
#반복: *
print("Python"*3)
#길이 변환: len()
print(len("Python"))
print("-------------------------")

#포함여부 확인: in
s="Python"
#시퀀스 내에 y가 있습니까?
print("y"in s)
#시퀀스 내에 j가 있지 않습니까?
print('j'not in s)
print("-------------------------")

#시퀀스 모델의 인덱스 접근
#'o'를 인덱스로 접근
print(s[4])
#'o'를 역인덱스로 접근
print(s[-2])
#시퀀스 모델의 추출 ytho추출
print(s[1:5])
#역인덱스로 추출
print(s[-5:-1])
print("-------------------------")

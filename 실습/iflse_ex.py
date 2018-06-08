#조건문 if ~elif~else

n=-2
if n>0:
    print("양수")
elif n<0:
    print("음수")
else:
    print("0")

#if는 중첩해서 사용할 수 있다.
#조건이 여러개일 경우: and, or등 논리 연산자를 이용해서 조건을 조합할 수 있다.

#조건표현식
#Java나 C의 3항 연산과 비슷
money = 12000
print("by taxi" if money>10000 else "by bus")
money = 0
print("by tax" if money >=1000 else "on foot" if money==0 else "by bus")

#in, not in: 포함 관계를 나타내는 연산
#리스트 내포도 같이 해봅시다.
source = [x for x in range(1,100,2)]
if 2 in source:
    print("2를 포함하고 있습니다.")
else:
    print("2를 포함하지 않습니다.")

print("source:",source)
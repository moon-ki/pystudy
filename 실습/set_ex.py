#세트
#   순서없고, 중복이 없는 객체의 집합니다.
#   {} 로 정의
#   in, not in, len 메소드사용
#   변경가능
#   수학의 집합 표현 시, 사용.

#세트 만들기
a={1,2,3}
print(a,type(a))

#포함여부 확인
print(2 in a)
print(3 in a)
print(2 not in a)
print(3 not in a)

#객체추가: add(x)
a.add(4)
print("a.add(4):",a)
a.add(4) #이미 있는 값을 추가
print("a.add(4)*2:",a)

#객체를 제거해 봅시다.: remove(x), discard(x)
a.remove(4)
print("a.remove(4):",a)
#a.remove(4) #KeyError: 4: 4가 없어서 제거할 수 없다.
#print("a.remove(4)*2:",a)
a.discard(4)
print("a.discard(4):",a) #4가 없어도 에러가 발생하지 않는다.

#셋트에 여러개의 값을 추가: update()
a.update({1,3,5,7,9})
print("a.update({1,3,5,7,9}):",a)

#집합 연산: 합집합, 교집합, 차집합
s1={1,2,3,4,5,6,7,8,9,10}
even={2,4,6,8,10}
odd={1,3,5,7,9}
mask={3,6,9}
#합집합
print("even.union(odd)==s1: ",even.union(odd)==s1) #짝수와 홀수의 합집합은 전체집합일까?
print("even|odd==s1:",even|odd==s1)
#교집합
print("odd.intersection(mask):",odd.intersection(mask)) #홀수집합과 3의 배수 집합의 교집합
print("sorted(odd.intersection(mask)):",sorted(odd.intersection(mask)))#함수를 쓰면 집합도 정렬 가능함.
print("odd&mask",odd&mask)
#차집합
print("s1.difference(even)==odd:",s1.difference(even)==odd) #전체집합-짝수집합=홀수집합?
print("s1-even==odd: ",s1-even==odd)
#모집합과 부분집합
print(s1.issuperset(even))  #s1은 even의 모집합인가?
print(even.issubset(s1))    #even의 s1 부분집합인가?
print({10,11,12}.issubset(s1))




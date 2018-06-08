#사전
#   순서 없고, key/value 매칭 자료형
#   순서가 없어서 index, slicing 안되고
#   len(), in, not in 가능

#사전 만들기
d=dict()
print(d,type(d))

#방법2:{} 이용하여 만들기
d={}
print(d,type(d))

#방법3:key/value arg 이용하여 만들기
d=dict(one=1,two=2)
print(d,type(d))

#방법4: key, value 리스트들이 따로 있을 때,
key = ("one", "two", "three")
values=(1,2,3)
d=dict(zip(key,values))
print(d,type(d))

#사전의 키
print("----------------------")

#변경불가 자료형을 사용해야함
d={}
d[10]="10"
d["baseball"]=9
d[("kim",10)]="학생"
print(d,type(d))

#d[["lee",30]] = "근로자" #unhashable type: 'list' 변경가능 자료형을 사용해서 

#사전 메서드
print("-----------Methos")
d={"baseball":9,"soccer":11,"basketball":5}
print(d,type(d))
#키목록을 가져와 보게습니다. : keys()
print(d.keys())
#값의 목록: values()
print(d.values())
#키와 값의 쌍의 목록: items()
print(d.items())

#값 가져오기
print(d["baseball"])
#print(d["handball"]) #KeyError: 'handball'

#값 가져오기2:get()
print(d.get("handball")) #에러는 발생하지 않지만, None 으로 출력
print(d.get("handball","?"))#없으면 ?으로 출력한다.

#값의 삭제: del 함수
del d['soccer']
print(d)

#사전 비우기
#d.clear()
#print(d)

#사전의 순회
print("-----------순회")
d["soccer"]=11
#방법1: 키값을 순회하면서 받아와 내용 처리
#for key in d: #아래와 같게 쓰일 수 있음
for key in d.keys():    
    print(key,":",d[key]) 

#방법2: 키와 값을 함께 받아와서 활용: items()
for key,value in d.items():
    print("{0}:{1}".format(key,value),end=" ")
else:#for문이 끝나면 개행
    print()    
#sys 모듈
#파이썬 인터프리터 관련 정보와 기능
#argv

import sys

def argv_f():
    print(sys.argv)
    args = sys.argv[1:]
    print("args:",args)
def env_f():
    #플랫폼 정보를 얻어온다.
    print(sys.platform) #win32
    #시스템 버전을 얻어온다.
    print(sys.version) #(v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)]
    #모듈 디렉토리 확인
    print(sys.path)
#env_f()

#random() 모듈
#임의의 특정 값을 선택 제공
#그 이외의 난수관련 유틸리티 함수

import random
#0~1사이의 난수발생
print(random.random())
#특정 범위의 정수 내에서 정수 난수 발생
print(random.randint(1,6))

#랜덤 유틸리티 함수
seq=["짬뽕","짜장면","짬짜면","탕수육"]
# 이 리스트를 섞어 봅시다: suffle
random.shuffle(seq)
print(seq)

#순차형에서 임의의 한개 객체 반환:choice
print(random.choice(seq))

#sampling
print(random.sample(range(1,46),6)) #1~46 사이의 순차 정수 중에서 6개 추출
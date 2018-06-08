import mymod
import math

#모듈명.객체 형식으로 사용할 수 있다.
print(math.pi)
print(mymod.pi)

r=10
print("Round:",math.pi*r**2)
print("Round:",mymod.pi*r**2)

#어떤 모듈이 현재 로드되어 있는가
import sys
#현재 로드된 모듈의 목록을 출력
#print(sys.modules)#dict이므로 특정 key값을 기준으로 어떤 모듈이 로드 되었는지 확인할 수 있음
moduls = sys.modules.keys()
print(moduls)
print("YES" if "mymod" in moduls else "NO")
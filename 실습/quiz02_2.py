""" 
lst = [1, 3.14, 'python', 7, 89.1, 3]

lst_cleaned=[]

for item in lst:
    #if isinstance(item,int) or isinstance(item,float):
    if isinstance(item,(int,float)):#item이 int 형이거나, float형이면
        lst_cleaned.append(item)
print(lst_cleaned) """

# 당 리스트에서 정수형, 실수형 데이터만 추출하여 lst_cleaned 라는 이름의 리스트에 담아 봅시다.

lst = [1, 3.14, 'python', 7, 89.1, 3]
lst_cleaned=[]
for tmp in lst:
    if isinstance(tmp, (int,float)):
        lst_cleaned.append(tmp)

print(lst_cleaned,type(lst_cleaned))
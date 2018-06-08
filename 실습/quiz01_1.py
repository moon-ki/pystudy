str = "Life is too short, You need Python"
#1
print(str.lower())
#2
print(str.lower().replace(" ","").replace(",",""))
#3
lists=list(str.lower().replace(" ","").replace(",",""))
print("list's type is",type(lists))
print("lists:",lists)
#4
char=set(lists) #set를 활용한 중복제거
#5
print("char:",char)
lst=list(char)
print("lst:",lst)
#6
lst.sort()
print("lst:",lst,", 길이:",len(lst))
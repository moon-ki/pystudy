""" def summary(*agrs):#가변인수를 받는 함수
    data=[]#가변인수를 담을 리스트
    total = 0
    for arg in agrs:
        if isinstance(arg,(int,float)):
            data.append(arg)
            total+=arg
    return total, max(data),min(data), total/len(data)


total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
print(total, maxval, minval, avg) """


def summary(*args):#*agrs는 리스트의 형태
    total=0
    lists=[]
    for arg in args:
        if isinstance(arg, (int,float)):
            total+=arg
            lists.append(arg)
        else:
            print("정수가 아닌 데이터입니다: ",arg)
    return total, max(lists), min(lists), total/len(lists)

total, maxval, minval, avg = summary(80, 75, 90, 95, 85,"dddd")
print(total, maxval, minval, avg)
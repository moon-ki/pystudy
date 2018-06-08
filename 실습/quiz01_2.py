lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sl = lst[3:7]       #4~7까지 가져온다.
print(sl)
#lst[3:7]=[]        #삭제
sl.reverse()        #추출값 반전
print("sl:",sl)     #확인
print("lst:",lst)   #확인
lst[3:7] = sl       #해당 자리에 데이터가 삭제되고 sl이 들어감
print(lst)

#사전으로 구성된 리스트!!
students = [
    {
    "name": "Kim",
    "kor": 80,
    "eng": 90,
    "math": 80
    },
    {
    "name": "Lee",
    "kor": 90,
    "eng": 85,
    "math": 85
    }
]

# 아래는 내가 생각해낸 방법이다.
# list의 각각의 데이터별로, 

i =  0
#print("len(students):",len(students)) #len(students): 2
while (i<len(students)):
    students[i]["total"]=students[i].get("kor")+students[i].get("eng")+students[i].get("math")
    students[i]["average"] = students[i]["total"] / 3
    print("students["+str(i)+"]:",students[i])
    i+=1
print(students)

#for(key in students.)

""" for student in students:
    total=student.get("kor")+student.get("eng")+student.get("math")
    average = total/3
    student["total"] = total
    student["average"]=average

print(students) """

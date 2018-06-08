#
def write01():
    #텍스트 파일쓰기
    f=open("./sample/test.txt","w",encoding="UTF-8")
    size = f.write("Life is too short, you need Python")
    print("write size:():",format(size))
    f.close()

#write01()

def read01():
    #텍스트 파일 읽기
    f=open("./sample/test.txt","r",encoding="UTF-8")
    text = f.read()
    print(text)
    f.close()

#read01()

def write02():
    #여러줄을 만들자
    f=open("./sample/mutilines.txt","w",encoding="utf-8")
    for i in range(1,10):
        f.write("Line %d\n" % i)
    f.close()    

#write02()

def read02():
    f=open("./sample/mutilines.txt","r",encoding="utf-8")
    text=f.read()#메모리에 파일의 모든 데이터를 올리기 떄문에 부하가 예상됨
    print(text)
    f.close()
#read02()

def read02_1():
    f=open("./sample/mutilines.txt","r",encoding="utf-8")
    #루프를 돌면서 한줄씩 read
    while True:
        line=f.readline()
        if not line :
            break
        print(line,end="")
    f.close
#read02_1()      

def read02_2():
    f=open("./sample/mutilines.txt","r",encoding="utf-8")
    lines=f.readlines()#list 형식으로 모든 라인을 받아옴
    line = lines[5]
    print(lines)
    f.close
#read02_2()

#sample 디렉토리 안에 sangbuk.csv 파일을 열고 
#각 줄을 dict으로 만들고 리스트에 저장해 봅시다.

def slamdunk():
    members = []
    f=open("./sample/sangbuk.csv","r",encoding="utf-8")
    while True:
        line=f.readline()
        if not line:
            break
        line=line.strip().replace(" ","")
        info=line.split(",")
        member = {"name":info[0], "number":info[1], "height":info[2],"position":info[3]}#member dict에 넣는다.
        members.append(member)

    print(members)    
    f.close()
#slamdunk()

#바이너리 파일 다루기 모드:b
def binfile():
    f_src = open("./sample/rose-flower.jpeg","rb")
    data=f_src.read()
    f_src.close

    f_dest=open("./sample/rose-flower-copy.jpeg","wb")
    f_dest.write(data)
    f_dest.close

binfile()

#파일은 open하면 반드시 닫아줘야 하는데
#with ~ as를 이용하면 파이썬이 사용 후 닫아준다.
def safe_file():
    with open("./sample/mutilines.txt","r") as f:
        for line in f.readlines():
            print(line,end=" ")
    print()
    #f가 닫혀있는지 확인
    print(f.closed)
#safe_file()    

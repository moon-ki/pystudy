
#클래스 만들기
class Point:
    instance_count = 0

    #생성자
    def __init__(self, x=0, y=0):
        self.x , self.y = x,y
        #클래스 영역의 접근
        Point.instance_count +=1
    def __del__(self):
        Point.instance_count -=1

    #__str__구현
    def __str__(self):
        return "Point x = {}, y={}".format(self.x, self.y)
    #__repr 구현    
    def __repr__(self):
        return "Point({},{})".format(self.x, self.y)

    #인스턴트 메서드
    def setX(self,x):
        self.x=x
    def getX(self):
        return self.x
    def setY(self,y):
        self.y = y
    def getY(self):
        return self.y

def bound_method():
    p = Point()# 객체생성
    p.setX(10)
    p.setY(10)
    print(p.getX(), p.getY(),set=",")
    print(p.getX(), p.getY())

if __name__ =="__main__":
    bound_method()

def unbound_method():
    p=Point()
    Point.setX(p,10)
    Point.setY(p,10)
    print(Point.getX(p), Point.getY(p), set=",")
    print(Point.getX, Point.getY)

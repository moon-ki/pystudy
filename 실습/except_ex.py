def try_f1():
    try:
        lst=[1,3,5,7,9]
        lst[5] #IndexError: list index out of range
    except:
        print("Error")
#try_f1()

def try_f2():
    try:
        value=int("10a")
        #ValueError: invalid literal for int() with base 10: '10a'
    except ValueError as e:
        print("변환할 수 없습니다.")    
    except Exception as e:
        print("Exception e:",e)
        print("type(e):",type(e))
#try_f2()

def try_f3():
    result = 4/0
    #ZeroDivisionError: division by zero
#try_f3()

def example():
    try:
        num1 = input("첫 번째 숫자를 입력해 주세요.")
        num2 = input("두번째 숫자를 입력해 주세요.")
        num1=int(num1)
        num2=int(num2)
        result = num1/num2
    except ValueError as e:
        print("정수형 문자가 아닙니다.")
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없습니다.")    
    except Exception as e:
        print("e:",e)
    else:       #오류가 없을 때, 실행
        print("{} / {} = {}".format(num1, num2, result))
    finally:    #항상 실행
        print("예외처리 완료")
#example()    

#특정 경우에는 외부에서 처리시키기 위해 일부러 예외를 발생시키기도 합니다.
def beware_dog(animal):
    if animal=="dog":
        #예외발생
        raise RuntimeError("멍멍")
    else:
        print("환영합니다.")
try:        
    beware_dog("cow")
    beware_dog("cat")
    beware_dog("dog")
except RuntimeError as e:
    print("e:",e)
    print(type(e))

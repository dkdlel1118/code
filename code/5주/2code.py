import time
def a(a,b):
    aa = (a+b)
    return aa
def aa(a,b):
    aa = (a-b)
    return aa
def aaa(a,b):
    aa = (a*b)
    return aa
def aaaa(a,b):
    aa = (a/b)
    return aa
while(1):
    print("1,2,3,4,중에서 골라주세요")
    print("1은 더하기입니다")
    print("2은 빼기입니다")
    print("3은 곱하기입니다")
    print("4은 나누기입니다")
    b=int(input('연산할 숫자를 선택해주세요 -> '))
    if b==1:
        print('더하기 연산을 시작합니다')
        print('----------------------')
        x=int(input('첫번째 숫자를 입력해주세요 -> '))
        print('----------------------')
        y=int(input('두번째 숫자를 입력해주세요 -> '))
        print("정답은 ->",a(x,y))
        print("계속 사용 하시겠습니까?")
        print("좋으시면 1 아니면 2 를 눌러주세요")
        b=int(input('숫자를 입력해주세요 -> '))
        if b==2:
            print('로딩 중 입니다')
            time.sleep(1)
            break
    elif b==2:
        print('빼기 연산을 시작합니다')
        print('----------------------')
        x=int(input('첫번째 숫자를 입력해주세요 -> '))
        print('----------------------')
        y=int(input('두번째 숫자를 입력해주세요 -> '))
        print("정답은 ->",aa(x,y))
        print("계속 사용 하시겠습니까?")
        print("좋으시면 1 아니면 2 를 눌러주세요")
        b=int(input('숫자를 입력해주세요 -> '))
        if b==2:
            print('로딩 중 입니다')
            time.sleep(1)
            break
    elif b==3:
        print('곱하기 연산을 시작합니다')
        print('----------------------')
        x=int(input('첫번째 숫자를 입력해주세요 -> '))
        print('----------------------')
        y=int(input('두번째 숫자를 입력해주세요 -> '))
        print("정답은 ->",aaa(x,y))
        print("계속 사용 하시겠습니까?")
        print("좋으시면 1 아니면 2 를 눌러주세요")
        b=int(input('숫자를 입력해주세요 -> '))
        if b==2:
            print('로딩 중 입니다')
            time.sleep(1)
            break
    elif b==4:
        print('나누기 연산을 시작합니다')
        print('----------------------')
        x=int(input('첫번째 숫자를 입력해주세요 -> '))
        print('----------------------')
        y=int(input('두번째 숫자를 입력해주세요 -> '))
        print("정답은 ->",aaaa(x,y))
        print("계속 사용 하시겠습니까?")
        print("좋으시면 1 아니면 2 를 눌러주세요")
        b=int(input('숫자를 입력해주세요 -> '))
        if b==2:
            print('로딩 중 입니다')
            time.sleep(1)
            break
    else:
        print("다시 입력해주세요")


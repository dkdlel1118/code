for i in range(5):



    print("1,2,3,4,중에서 골라주세요")
    print("1은 더하기입니다")
    print("2은 빼기입니다")
    print("3은 곱하기입니다")
    print("4은 나누기입니다")

    a=int(input('연산할 숫자를 선택해주세요 -> '))

    if a==1:
        print('더하기 연산을 시작합니다')
        print('----------------------')
        x=int(input('첫번째 숫자를 입력해주세요 -> '))
        print('----------------------')
        y=int(input('두번째 숫자를 입력해주세요 -> '))

        print("정답은->",x+y)
    elif a==2:


        x=int(input())
        y=int(input())

        print(x-y)
    elif a==3:

        x=int(input())
        y=int(input())

        print(x*y)
    elif a==4:




        x=int(input())
        y=int(input())

        print(x/y)
    else:

        print("1,2,3,4,중에서 골라주세요")







import random

a= random.randint(1,1000)
b=None
for i in range(8):
    c=int(input('맞추실 숫자를 입력해주세요->'))
    if a<c:
        print('이거보다는 작습니다')
    if a>c:
        print('이거보다는 큽니다')
    if c==a:
        print('축하합니다 맞추셨습니다')
        break
print("죄송하지만 기회를 모두 소진 하셨습니다")


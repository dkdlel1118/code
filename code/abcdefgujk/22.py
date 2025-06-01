import random

g = 10000

h = int(input('시작하고 싶으시다면 0을 눌러 주세요 -> '))
while h == 0:
    # 슬롯 3개 뽑기
    slots = [random.randint(1, 10) for _ in range(3)]
    print("슬롯 결과:", slots)
    count_7 = slots.count(7)

    if count_7 == 3:
        print("축하합니다 럭키 777에 당첨 됬습니다")
        g += 1000
        g -= 15
    elif count_7 == 2:
        print("축하합니다 럭키 77에 당첨 됬습니다")
        g += 150
        g -= 15
    elif count_7 == 1:
        print("축하합니다 럭키 7에 당첨 됬습니다")
        g += 20
        g -= 15
    else:
        print('아쉽지만 다음 기회에')
        g -= 15

    print("현재 골드는", g, "입니다")
    h = int(input('멈추고 싶으시다면 1을 눌러주세요 -> '))
    if h == 1:
        break
    else:
        print('')
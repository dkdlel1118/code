import time

print("이 기계는 평균을 구하는 기계입니다")
print("국,영,수,과의 평균을 구할수 있습니다")
a=int(input('국어의 점수를 입력해주세요 -> '))
print("국어의 점수가 확인 되었습니다")
b=int(input('영어의 점수를 입력해주세요 -> '))
print("영어의 점수가 확인 되었습니다")
c=int(input('수학의의 점수를 입력해주세요 -> '))
print("수학의 점수가 확인 되었습니다")
d=int(input('과학의 점수를 입력해주세요 -> '))
print("과학의 점수가 확인 되었습니다")
print("잠시만 기다려 주세요")
time.sleep(2)
print((a+b+c+d)/4)
time.sleep(0.5)
print("이용해주셔서 감사합니다")
time.sleep(0.5)
print("다음에 또 이용해주세요")

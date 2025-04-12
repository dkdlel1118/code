import time

count = int( input("문자열1 :"))
numbers =  input("문자열2 :").split()
print("로딩중")
time .sleep(1)
for num_str in numbers:
        num = int(num_str)
        result = 1
        for i in range(1, num +1 ):
            result *= i
        print(num, "의 팩토리엄 ", result, "입니다")



















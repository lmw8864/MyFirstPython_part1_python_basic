# 10-6.py

"""
10-6. 덧셈
"""
print("더할 숫자를 두 개 입력하세요.")
num1 = input("First number: ")
num2 = input("Second number: ")

try:
    sum = int(num1) + int(num2)
except ValueError:
    print("값을 잘못 입력하셨습니다. 숫자를 입력해 주세요.")
else:
    print(sum)

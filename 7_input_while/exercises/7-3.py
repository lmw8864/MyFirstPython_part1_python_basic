# 7-3.py

"""
7-3. 10의 배수
"""

number = input("숫자를 입력하시면 17의 배수인지 알려드릴게요: ")
if int(number) % 17 == 0:
    print(number + " 은(는) 17의 배수가 맞네요!")
else:
    print(number + " 은(는) 17의 배수가 아닙니다.")

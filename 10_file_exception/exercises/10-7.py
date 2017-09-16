# 10-7.py

"""
10-7. 덧셈 계산기
"""

while True:
    print("더할 숫자를 두 개 입력하세요.(종료하시려면 'q' 입력)")
    num1 = input("First number: ")
    if num1 == 'q':
        break
    num2 = input("Second number: ")
    if num2 == 'q':
        break

    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("값을 잘못 입력하셨습니다. 숫자를 입력해 주세요.")
    else:
        print(sum)

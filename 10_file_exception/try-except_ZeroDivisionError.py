# try-except_ZeroDivisionError.py

"""
예외(exception)

    - 예외는 try-except 블록에서 처리
    - 어떤 동작을 지시하고, 예외가 생겼을 때 할 일도 지시
    - 설령 뭔가 잘못되더라도 프로그램은 계속 실행된다.
    - 트레이스백 대신 알기 쉬운 에러 메시지를 표시할 수 있음
"""

# 0으로 나눈 에러
# print(5/0)
# Traceback (most recent call last):
#   File "D:/Users/Minwoo_Lee/Documents/ImaDeveloper/myFirstPython/part1/10_file_exception/try-except_ZeroDivisionError.py", line 14, in <module>
#     print(5/0)
# ZeroDivisionError: division by zero


# try-except 블록 (0으로 나눈 예외 처리)
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")  # Traceback 대신 알기 쉬운 에러 메시지 출력

# You can't divide by zero!


# 예외를 써서 충돌 막기
# 정확한 에러 처리는 에러가 일어난 후에 프로그램이 할 일이 더 있을 때 특히 중요
# 사용자 입력을 받는 프로그램에서 자주 필요

# 나눗셈만 하는 단순한 계산기 예제
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#
#     answer = int(first_number) / int(second_number)
#     print(answer)

# Give me two numbers, and I'll divide them.
# Enter 'q' to quit.
#
# First number: 5
#
# Second number: 0
# Traceback (most recent call last):
#   File "D:/Users/Minwoo_Lee/Documents/ImaDeveloper/myFirstPython/part1/10_file_exception/try-except_ZeroDivisionError.py", line 46, in <module>
#     answer = int(first_number) / int(second_number)
# ZeroDivisionError: division by zero

# --> 이 프로그램에는 에러 처리가 전혀 없으므로 0으로 나누게 하면 충돌함.


# else 블록
# 에러를 일으킬 수 있는 행을 try-except 블록으로 감싼다.
# try 블록이 성공할 때만 실행할 코드는 모두 else 블록에 들어간다.


while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)  # try 블록이 성공할 때만 실행할 코드

# First number: 5
#
# Second number: 0
# You can't divide by 0!
#
# First number: 5
#
# Second number: 2
# 2.5
#
# First number: q

# ※ try 문에는 예외를 일으킬 수 있는 코드만 쓴다.
# 어떤 에러가 일어날지 예상한다면 잘못된 데이터를 받았거나 필요한 자원이 없을 때도 프로그램이 계속 동작하게 만들 수 있다.

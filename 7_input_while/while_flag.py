# whie_flag.py

# 플래그 사용하기
"""
프로그램을 멈추게 해야하는 조건이 여러가지라면?
    - 변수 하나를 정의해 전체 프로그램을 계속할지 끝낼지 판단할 수 있습니다.
    - 이런 변수를 '플래그(flag)'라 부르며 프로그램에 대한 '신호'처럼 동작합니다.
"""
prompt = "\nTell me something, and I will repeat it back to you.\n(Enter 'quit' to end the program.): "

# active 변수를 flag 로 사용
active = True  # flag 초깃값 지정
while active:
    message = input(prompt)

    # 'quit' 입력 시 flag 를 False 로 만들어서 while 루프 종료
    if message == 'quit':
        active = False
    else:
        print(message)

# Tell me something, and I will repeat it back to you.
# (Enter 'quit' to end the program.): 123
# 123
#
# Tell me something, and I will repeat it back to you.
# (Enter 'quit' to end the program.): quit

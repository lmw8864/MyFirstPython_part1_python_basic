# while_loop.py

# while 루프 사용하기
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# 사용자가 멈출 수 있도록 만들기
prompt = "\nTell me something and I will repeat it back to you."
prompt += "\n(Enter 'quit' to end the program.): "

message = " "  # message 에 초깃값 지정
# 비교할 대상이 없으면 while 루프로 진입할 수가 없어서 빈 문자열을 만들어 주는 것

while message != 'quit':
    message = input(prompt)

    if message != 'quit':  # 사용자가 'quit'를 입력하면 메시지 출력하지 않기
        print(message)

# Tell me something and I will repeat it back to you.
# (Enter 'quit' to end the program.): 사랑합니다
# 사랑합니다
#
# Tell me something and I will repeat it back to you.
# (Enter 'quit' to end the program.): 느므 조아요
# 느므 조아요
#
# Tell me something and I will repeat it back to you.
# (Enter 'quit' to end the program.): quit

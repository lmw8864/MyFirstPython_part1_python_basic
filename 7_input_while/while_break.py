# while_break.py

"""
조건 테스트 결과와 상관없이 사용자가 'quit'를 입력하는 즉시 break를 호출해서 while 루프를 멈출 수 있다.
"""

prompt = "\nPlease enter the name of a city you have visited.(Enter 'quit' when you are finished.): "

while True:  # while 루프 무한히 실행
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Please enter the name of a city you have visited.(Enter 'quit' when you are finished.): paris
# I'd love to go to Paris!
#
# Please enter the name of a city you have visited.(Enter 'quit' when you are finished.): quit

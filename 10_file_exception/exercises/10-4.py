# 10-4.py

"""
10-4. 방명록
"""

while True:
    name = input("성함을 입력하세요.(종료하시려면 'q'를 입력): ")
    if name == 'q':
        break
    message = name + "님, 환영합니다!"
    print(message)

    with open('guest_book.txt', 'a') as f:
        f.write(name + "\n")

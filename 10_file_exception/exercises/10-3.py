# 10-3.py

"""
10-3. 손님
"""

# 이어붙이기 모드
with open('guest.txt', 'a') as f:
    name = input("성함을 입력하세요.: ")
    f.write(name + "\n")

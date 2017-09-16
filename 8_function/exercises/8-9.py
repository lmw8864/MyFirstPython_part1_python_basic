# 8-9.py

"""
8-9. 마술사
"""


def show_magicians(magicians):
    """리스트에 있는 마술사 이름을 출력합니다."""
    for magician in magicians:
        print(magician.title())

magicians = ['이은결', '최현우', '오은영']

show_magicians(magicians)

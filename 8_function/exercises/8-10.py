# 8-10.py

"""
8-10. 훌륭한 마술사
"""


def show_magicians(magicians):
    """리스트에 있는 마술사 이름을 출력합니다."""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """각 마술사의 이름 앞에 '훌륭한'을 추가합니다."""
    i = 0
    while i < len(magicians):
        magicians[i] = "훌륭한 " + magicians[i]
        i += 1


magicians = ['이은결', '최현우', '오은영']
make_great(magicians)
show_magicians(magicians)

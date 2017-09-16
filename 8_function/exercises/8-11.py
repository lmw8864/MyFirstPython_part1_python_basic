# 8-11.py

"""
8-11. 변하지 않은 마술사
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
    return magicians


magicians = ['이은결', '최현우', '오은영']

great_magicians = make_great(magicians[:])  # 리스트의 사본을 함수에 전달 → 반환된 리스트를 새 리스트에 저장

# 마술사 리스트(원본)
show_magicians(magicians)  # 이은결    최현우    오은영

# 훌륭한 마술사 리스트(수정본)
show_magicians(great_magicians)  # 훌륭한 이은결    훌륭한 최현우    훌륭한 오은영

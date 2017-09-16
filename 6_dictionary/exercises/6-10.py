# 6-10.py

"""
6-10. 좋아하는 숫자
"""

favorite_numbers = {
    '일라이': [1, 5],
    '이루마': [2, 4],
    '삼순이': [3, 6, 9],
    '사랑이': [4, 4, 16, 32],
    '오나미': [5, 55, 555],
}

for name, numbers in favorite_numbers.items():
    print("\n" + name + "가 좋아하는 숫자: ")
    for number in numbers:
        print(str(number))

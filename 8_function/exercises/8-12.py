# 8-12.py

"""
8-12. 샌드위치
"""


def make_sandwich(*sandwich_fillings):
    """샌드위치 안에 넣을 재료를 출력합니다."""
    print("\n샌드위치 안에 넣을 재료:")
    for sandwich_filling in sandwich_fillings:
        print("\t- " + sandwich_filling)

make_sandwich('햄', '치즈', '베이컨')
make_sandwich('에그 마요', '치즈')
make_sandwich('치킨', '치즈', '아보카도', '페퍼로니')

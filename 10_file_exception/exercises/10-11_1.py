# 10-11_1.py

"""
10-11_1. 좋아하는 숫자를 묻고 저장합니다.
"""

import json

favorite_number = input("좋아하는 숫자를 입력하세요.: ")
filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

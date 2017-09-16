# 10-12.py

"""
10-12. 좋아하는 숫자 기억
"""

import json

filename = 'favorite_number2.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("좋아하는 숫자를 입력하세요.: ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
else:
    print("당신이 좋아하는 숫자는 " + favorite_number + " 입니다.")

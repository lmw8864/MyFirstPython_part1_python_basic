# 10-11_2.py

"""
10-11_2. 좋아하는 숫자 메시지를 출력합니다.
"""

import json

filename = 'favorite_number.json'
with open(filename) as f:
    favorite_number = json.load(f)
    print("당신이 좋아하는 숫자는 " + favorite_number + " 입니다.")

# 7-2.py

"""
7-2. 레스토랑 예약
"""

customer_numner = input("일행이 몇 명이세요? ")
customer_numner = int(customer_numner)

if customer_numner >= 9:
    print("9명 이상이면 자리가 날 때까지 기다리셔야 됩니다.")
else:
    print("가능한 테이블이 있습니다.")

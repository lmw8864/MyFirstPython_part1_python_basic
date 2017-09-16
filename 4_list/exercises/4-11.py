# 4-11.py

"""
4-11. 내 피자, 네 피자
"""

favorite_pizzas = ['단호박 피자', '페페로니 피자', '씨푸드 피자', '고르곤졸라 피자']
for pizza in favorite_pizzas:
    print(pizza)
print("\n")

for pizza in favorite_pizzas:
    print("나는 " + pizza + "를 좋아합니다.")
print("\n")

for pizza in favorite_pizzas:
    print("나는 " + pizza + "를 좋아합니다.")
print("근데 피자는 가끔 먹어야 맛있어요..")

print("\n")

# 피자 리스트 복사
friend_pizzas = favorite_pizzas[:]

# 원래 리스트에 새 피자 추가
favorite_pizzas.append('포테이토 피자')

# friend_pizzas 리스트에 다른 피자를 추가
friend_pizzas.append('불고기 피자')

print("내가 좋아하는 피자는: ")
for pizza in favorite_pizzas:
    print(pizza)

print("\n내 친구가 좋아하는 피자는: ")
for pizza in friend_pizzas:
    print(pizza)

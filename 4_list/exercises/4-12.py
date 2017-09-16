# 4-12.py

"""
4-12. 루프
"""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

print("\nMy favorite foods are: ")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are: ")
for food in friend_foods:
    print(food)

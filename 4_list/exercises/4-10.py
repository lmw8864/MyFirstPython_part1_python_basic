# 4-10.py

"""
4-10. 슬라이스
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)  # ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nMy friend's favorite foods are: ")
print(friend_foods)

print("\n리스트의 첫 세 항목은: ")
for food in my_foods[:3]:
    print(food)

print("\n리스트의 중간 두 항목은: ")
for food in my_foods[1:3]:
    print(food)

print("\n리스트의 마지막 세 항목은: ")
for food in my_foods[-3:]:
    print(food)

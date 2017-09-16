# list_slice.py

# 리스트 자르기
players = ['charles', 'martina', 'florence', 'eli']
print(players[0:3])  # ['charles', 'martina', 'florence'] → 인덱스 0, 1, 2
print(players[1:4])  # ['martina', 'florence', 'eli'] → 인덱스 1, 2, 3
print(players[:4])  # ['charles', 'martina', 'florence', 'eli'] → 처음부터 인덱스 3까지
print(players[2:])  # ['florence', 'eli'] → 인덱스 2부터 끝까지
print(players[-3:])  # ['martina', 'florence', 'eli'] → 리스트의 마지막 3개 항목 출력

# ※ range() 함수처럼 마지막 인덱스는 포함되지 않음.

print("\n")

# 슬라이스에 루프 실행하기
players = ['charles', 'martina', 'florence', 'eli']

print("Here are the first three players on my team: ")
for player in players[0:3]:
    print(player.title())
# Here are the first three players on my team:
# Charles
# Martina
# Florence

print("\n")

# 리스트 복사하기 [:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake']
#
# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

print("\n")

# 실제로 리스트가 두 개 존재하는지 확인해보자.
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']
#
# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']

print("\n")

# ※ 혹시 그러면 슬라이스없이 friend_foods = my_foods 라고 하면 안될까?
my_foods = ['pizza', 'falafel', 'carrot cake']

# 이 코드는 원하는대로 동작하지 않음.
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
#
# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# ※ 파이썬에서 '=' 는 단순히 연결하는 기능만 한다. 즉, 두 변수는 같은 리스트를 가리킨다.

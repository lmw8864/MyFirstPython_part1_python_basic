# dictionary_nesting_1.py

"""
딕셔너리를 리스트에,
리스트를 딕셔너리에,
딕셔너리를 다른 딕셔너리에 저장할 수 있다.

1. 딕셔너리를 리스트에 저장하기
"""

# 리스트 안에 딕셔너리 담기
alien_0 = {'clolr': 'green', 'points': 5}
alien_1 = {'clolr': 'yellow', 'points': 10}
alien_2 = {'clolr': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
# {'clolr': 'green', 'points': 5}
# {'clolr': 'yellow', 'points': 10}
# {'clolr': 'red', 'points': 15}


print("\n")
# 빈 리스트에서 range()를 써서 외계인 30명으로 구성된 함대를 만들어보자.
aliens = []  # 외계인을 저장할 빈 리스트

# 녹색 외계인 30명 만드는 루프
for alien_number in range(30):  # range(0, 30)
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 처음 다섯명만 출력
for alien in aliens[:5]:        # aliens[0] ~ [4]
    print(alien)
print("...")

# 외계인이 총 몇 명 만들어졌는지 출력
print("Total number of aliens: " + str(len(aliens)))  # str()함수 잊지말자!

# {'points': 5, 'speed': 'slow', 'color': 'green'}
# {'points': 5, 'speed': 'slow', 'color': 'green'}
# {'points': 5, 'speed': 'slow', 'color': 'green'}
# {'points': 5, 'speed': 'slow', 'color': 'green'}
# {'points': 5, 'speed': 'slow', 'color': 'green'}
# ...
# Total number of aliens: 30


print("\n")
# 외계인 중 처음 셋을 노란색의 중간속도, 10점짜리 외계인으로 바꿔보자.
for alien in aliens[:3]:  # 0, 1, 2
    # 지금은 모든 외계인이 녹색이지만, 항상 그렇다고 보장할 수 없으므로 if문을 써서 수정
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 처음 5명 출력...
for alien in aliens[0:5]:
    print(alien)
print("...")
# {'points': 10, 'speed': 'medium', 'color': 'yellow'}
# {'points': 10, 'speed': 'medium', 'color': 'yellow'}
# {'points': 10, 'speed': 'medium', 'color': 'yellow'}
# {'points': 5, 'speed': 'slow', 'color': 'green'}
# {'points': 5, 'speed': 'slow', 'color': 'green'}
# ...


print("\n")
# elif 블록으로 확장해 노란색 외계인을 빨갛고 빠르게 움직이는 15점짜리로 수정.
for alien in aliens[:3]:  # 0, 1, 2
    # if문 쓰기 잘했네~
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 처음 5명 출력...
for alien in aliens[0:5]:
    print(alien)
print("...")
# {'points': 15, 'speed': 'fast', 'color': 'red'}
# {'points': 15, 'speed': 'fast', 'color': 'red'}
# {'points': 15, 'speed': 'fast', 'color': 'red'}
# {'points': 5, 'speed': 'slow', 'color': 'green'}
# {'points': 5, 'speed': 'slow', 'color': 'green'}
# ...

# ※ 한 객체에 관한 정보를 담고 있는 딕셔너리가 여러 개 있다면, 그 딕셔너리들을 리스트 하나에 저장할 때가 많다.
# 예를 들어, 웹사이트의 각 사용자마다 딕셔너리를 만들고 각 딕셔너리를 users 리스트에 저장할 수 있다.
# 리스트에 들어있는 딕셔너리는 모두 완전히 같은 구조여야 리스트에 루프를 실행하면서 각 딕셔너리 객체를 같은 방법으로 다룰 수 있다.

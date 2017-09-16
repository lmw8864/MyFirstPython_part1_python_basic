# dictionary.py

alien_0 = {'키': '값', 'color': 'green', 'points': 5}

# 딕셔너리 값에 접근하기
print(alien_0['color'])     # green


# 새 키-값 쌍 추가하기
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  # {'color': 'green', '키': '값', 'x_position': 0, 'points': 5, 'y_position': 25}
# 파이썬은 각 키-값 쌍을 저장한 순서는 신경쓰지 않고 각 키와 값의 연결만 중시한다.


# 빈 딕셔너리로 시작하기
alien_0 = {}

alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)  # {'color': 'green', 'point': 5}


# 딕셔너리로 값 수정하기
alien_0['color'] = 'green'
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')

# The alien is green.
# The alien is now yellow.


print("\n")

# 재밌는 예제~
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Orininal x-position: " + str(alien_0['x_position']))

# 외계인 무브~!
# 현재 속도를 기준으로 외계인이 얼마나 빨리 움직이는지를 판단
alien_0['speed'] = 'fast'  # 외계인의 속도를 수정
if alien_0['speed'] == 'slow':
    x_increment = 1  # 증가분
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 이 외계인은 빠른 놈!
    x_increment = 3

# 새 위치는 이전 위치에 증가분을 더한 값
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Orininal x-position: 0
# New x-position: 3


# 키-값 쌍 제거하기 (del 문)
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)  # {'points': 5, 'color': 'green'}

del alien_0['points']
print(alien_0)  # {'color': 'green'}


# 비슷한 객체의 딕셔너리
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    # 마지막 키-값 쌍 다음에 쉼표를 남겨두는 건 다음 행에 새 키-값 쌍을 쓰기 쉽게 하는 좋은 습관이다.
    # }  # 책에는 이렇게 되어 있지만 아래행처럼 써도 된다.
}

print("Sarah`s favorite language is " +
      favorite_languages['sarah'].title() +
      ".")
# Sarah`s favorite language is C.

# if_test.py

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# Audi
# BMW
# Subaru
# Toyota


# 일치하는지 체크할 때 대소문자 무시하고 값만 비교하고 싶다면?
car = 'Audi'
print(car == 'audi')  # False

print(car.lower() == 'audi')  # True
print(car)  # Audi (실제 변수에는 아무런 영향을 주지 않고 체크할 수 있다.)


# 불일치 체크하기 (!=)
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
# That is not the correct answer. Please try again!


# 여러 조건 체크하기 (and, or)
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # False
print(age_0 >= 21 or age_1 >= 21)  # True


# 값이 리스트에 있는지 체크하기 (in)
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' in requested_toppings)  # False


# 값이 리스트에 없는지 체크하기 (not in)
banned_champions = ['shen', 'alistar', 'ryze']
champion = 'your fingers'

if champion not in banned_champions:
    print("Please, ban your fingers.")
# Please, ban your fingers.


# 불리언 표현식
# 불리언 값은 프로그램의 상태나 프로그램에 중요한 특정 조건, 예를 들어 게임이 실행 중인지,
# 사용자가 웹사이트의 특정 콘텐츠를 편집할 수 있는지 같은 조건을 저장할 때 자주 사용합니다.
game_active = True
can_edit = False

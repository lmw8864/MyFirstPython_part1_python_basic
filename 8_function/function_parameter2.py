# function_parameter2.py

"""
매개변수를 임의의 숫자만큼 전달하기

    매개변수를 몇 개나 받을지 미리 알 수 없을 때 매개변수 앞에 '*'를 붙여주면
    파이썬이 매개변수명의 빈 튜플을 만들고 받는 값을 모두 이 튜플에 저장한다.

     - 매개변수로 *toppings 를 지정하면,
        → 파이썬이 toppings 라는 빈 튜플을 만들고 받는 값을 모두 저장함.
"""


def make_pizza(*toppings):
    """주문받은 토핑 리스트 출력"""
    print(toppings)

make_pizza('pepperoni')  # 하나의 값을 받더라도 튜플로 저장한다.
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# ('pepperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """만들려고 하는 피자를 요약합니다."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# Making a pizza with the following toppings:
# - pepperoni
#
# Making a pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese


print("\n")
# 위치형 매개변수와 임의의 매개변수 함께 쓰기


def make_pizza(size, *toppings):
    """만들려고 하는 피자를 요약합니다."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# Making a 16-inch pizza with the following toppings:
# - pepperoni
#
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese

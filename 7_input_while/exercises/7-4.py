# 7-4.py

"""
7-4. 피자 토핑
"""
prompt = "피자에 추가할 토핑을 입력해주세요.('quit'를 입력하시면 종료됩니다): "
toppings = []

while True:
    topping = input(prompt)

    if topping != 'quit':
        toppings.append(topping)
        print("피자에 " + topping.title() + "을(를) 추가하겠습니다.")
    elif topping == 'quit':
        break

print("\n피자에 추가할 토핑 목록: ")
for topping in toppings:
    print(topping.title())

# 피자에 추가할 토핑을 입력해주세요.('quit'를 입력하시면 종료됩니다): pepperoni
# 피자에 Pepperoni을(를) 추가하겠습니다.
# 피자에 추가할 토핑을 입력해주세요.('quit'를 입력하시면 종료됩니다): black olive
# 피자에 Black Olive을(를) 추가하겠습니다.
# 피자에 추가할 토핑을 입력해주세요.('quit'를 입력하시면 종료됩니다): cheese
# 피자에 Cheese을(를) 추가하겠습니다.
# 피자에 추가할 토핑을 입력해주세요.('quit'를 입력하시면 종료됩니다): pepper
# 피자에 Pepper을(를) 추가하겠습니다.
# 피자에 추가할 토핑을 입력해주세요.('quit'를 입력하시면 종료됩니다): mushroom
# 피자에 Mushroom을(를) 추가하겠습니다.
# 피자에 추가할 토핑을 입력해주세요.('quit'를 입력하시면 종료됩니다): quit
#
# 피자에 추가할 토핑 목록:
# Pepperoni
# Black Olive
# Cheese
# Pepper
# Mushroom

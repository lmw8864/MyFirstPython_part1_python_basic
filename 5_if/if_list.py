# if_list.py

# 특별한 항목이 있는지 체크하기
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# Adding mushrooms.
# Sorry, we are out of green peppers right now.
# Adding extra cheese.
#
# Finished making your pizza!


print("\n")
# 리스트가 비어있지 않은지 확인하기
# for 루프를 쓰기 전에 리스트가 비어있지 않은지 체크하는 게 좋다.
requested_toppings = []  # 빈 리스트

if requested_toppings:
    for requested_topping in requested_toppings:
            print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# Are you sure you want a plain pizza?


print("\n")
# 여러 리스트 다루기
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

# Adding mushrooms.
# Sorry, we don't have french fries.
# Adding extra cheese.
#
# Finished making your pizza!

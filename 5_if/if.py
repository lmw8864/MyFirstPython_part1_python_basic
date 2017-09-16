# if.py

# 단순한 if문
age = 19

if age >= 18:
    print("You are old enough to vote!")
# You are old enough to vote!


# if-else 문
age = 17

if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")
# Sorry, you are too young to vote.


# if-elif-else 문
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
# Your admission cost is $5.

# ※코드를 간결하게~
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
# Your admission cost is $5.
# price를 str()로 감싸주는 것 유의!


# elif 블록 여러 개 쓰기
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")


# else 블록 생략하기
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")
# ※else 블록은 앞에 있는 if나 elif가 일치하지 않았다면 무조건 실행되므로,
# 잘못된 데티터나 심지어 악의적인 데이터도 체크하지 않고 받아들일 가능성이 있다.
# 특정 조건을 마지막으로 테스트해야 한다면 마지막에 elif 블록을 쓰고 else 블록은 생략한다.
# 이렇게 하면 코드가 더 정확한 조건에서만 실행될 수 있다.


# 여러 조건 테스트하기
# if-elif-else 문은 한 가지 조건을 만족하면 나머지를 모두 무시한다.(건너뜀)
# 하지만 원하는 조건을 모두 체크해야한다면? - 단순한 if문을 여러 개 쓴다.
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
# Adding mushrooms.
# Adding extra cheese.

# 만약 if-elif 문을 썼다면 mushrooms 만 넣고 나머지는 체크하지도 않고 넘어갔을 것!

# ※코드 블록 단 하나만 실행해야 할 때는 if-elif-else 문을,
# 코드블록을 둘 이상 실행해야 한다면 독립적 if문을 여러 개 쓰세요.

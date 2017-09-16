# input.py

name = input("Pease enter your name: ")
print("Hello " + name + "!")

# 여러 줄의 프롬프트가 필요할 때엔?
# 프롬프트를 변수에 저장하고 그 변수를 input() 함수에 넘긴다.
# prompt = "If you tell us who you are we can personalize the messages you see.\nWhat is your first name? "
prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello " + name + "!")


# input() 함수를 써서 숫자형 입력받기
age = input("How old are you? ")
# print(age >= 20)
# TypeError: unorderable types: str() >= int()

print(int(age) >= 20)
# How old are you? 33
# True


# rollercoaster.py
height = input("How tall are you in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# How tall are you in inches? 71
#
# You're tall enough to ride!


# 나머지 연산자(%)
print(4 % 3)  # 1

# even_or_odd.py

number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# Enter a number and I'll tell you if it's even or odd: 55
#
# The number 55 is odd.

# ※ 비교할 때에는 int()로 변환했다가, 출력할 때는 다시 str()로 변환하는 것에 유의

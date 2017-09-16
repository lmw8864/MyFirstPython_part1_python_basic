# function_1.py

"""
함수 정의

독스트링(docstring)
매개변수(parameter)
    위치형 매개변수: 순서대로
    키워드 매개변수: 키-값 쌍으로 명시
    기본값(default value)
    매개변수 불일치 에러
"""


# 함수 정의
def greet_user():
    """간단한 환영 인사를 표시합니다."""  # docstring: 함수가 무슨 일을 하는지 설명하는 주석
    print("Hello!")

greet_user()  # 함수 호출

# 아무리 간단한 함수라도 독스트링을 작성하는 게 좋다.


# 매개변수(parameter)
def greet_user(username):
    """간단한 환영 인사를 표시합니다."""
    print("Hello!, " + username.title() + "!")

greet_user('jesse')  # 함수 호출(매개변수 전달)
# Hello!, Jesse!


# 위치형 매개변수: 순서대로
def describe_pet(animal_type, pet_name):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')  # 함수 호출(정의한 순서대로 매개변수 전달)
# I have a hamster.
# My hamster's name is Harry.

# ※ 위치형 매개변수는 원하는만큼 많이 쓸 수 있다. 순서가 틀리지 않도록 주의한다.


# 키워드 매개변수: 키-값 쌍
def describe_pet(animal_type, pet_name):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')  # 함수 호출(매개변수를 명시적으로 지정)
# I have a hamster.
# My hamster's name is Harry.

describe_pet(pet_name='harry', animal_type='hamster')  # 매개변수 순서를 바꿔써도 동일한 결과 반환
# I have a hamster.
# My hamster's name is Harry.

# ※ 키워드 매개변수는 순서에 상관이 없고, 정의한 매개변수 이름을 정확히 쓰는 게 중요함.


# 매개변수에 기본값(default value) 정의
def describe_pet(pet_name, animal_type='dog'):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry')  # 함수 호출(기본값을 정의한 매개변수를 생략하고 전달)
# I have a dog.
# My dog's name is Harry.

# ※ 함수를 정의할 때, 기본값을 정의해준 매개변수는 뒤에 적어주도록 한다.
# 위치형 매개변수로 전달할 때 기본값을 정의한 매개변수가 앞에 위치하면 생략할 수 없다.
# 생략하면 파이썬이 혼란스러워 함..@_@

describe_pet('harry')  # animal_type=’dog’를 뒤쪽에 정의해서 순서에 신경쓰지 않고 마음대로 생략이 가능하다.


# 위 함수에 대해 같은 결과를 반환하는 호출
describe_pet('whillie')
describe_pet('whillie', 'dog')

describe_pet(pet_name='whillie')
describe_pet(pet_name='whillie', animal_type='dog')
describe_pet(animal_type='dog', pet_name='whillie')
# I have a dog.
# My dog's name is Whillie.

# ※ 함수 호출 스타일은 중요하지 않음. 원하는 결과가 나온다면 가장 이해하기 쉬운 스타일을 쓸 것


# 매개변수 불일치 에러
def describe_pet(pet_name, animal_type='dog'):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet()
# TypeError: describe_pet() missing 1 required positional argument: 'pet_name'

# 함수가 동작할 때 필요한 것보다 적거나 많은 매개변수를 전달하면 매개변수 불일치 에러가 발생한다.

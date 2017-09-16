# json_module.py

"""
데이터 저장

    json 모듈
    - json.dump(저장할 데이터, 데이터를 저장할 파일 객체)
    - json.load(불러올 파일 객체)

    리팩토링(refactoring)
"""

# 숫자 리스트 저장하기 # json.dump()
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)  # numbers 리스트를 numbers.json 파일에 저장


# 파일에 저장된 리스트 불러오기 # json.load()
# import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)  # numbers.json 파일에 저장된 정보를 numbers 변수에 저장

print(numbers)  # [2, 3, 5, 7, 11, 13]


print("\n")
# 사용자가 생성한 데이터 저장하고 읽기

# 1. 사용자 이름을 저장하는 프로그램
# import json

# username = input("What is your name?: ")
# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print("We'll remember you when you come back, " + username.title() + "!")

# What is your name?: minwoo lee
# We'll remember you when you come back, Minwoo Lee!


print("\n")
# 2. 저장된 사용자를 환영하는 프로그램
# import json

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
    print("Welcome back, " + username + "!")

# Welcome back, minwoo lee!


print("\n")
# 두 프로그램 합치기 # try 문
# import json

# 사용자 이름이 저장됐다면 불러옵니다.
# 그렇지 않다면 사용자 이름을 묻고 저장합니다.
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

# try 블록에서는 username.json 파일을 열 수 있는지 시도한다.
# 이 파일이 존재하면 사용자 이름을 메모리로 불러오고, else 블록에서 사용자를 환영하는 메시지를 출력한다.
# 파일이 존재하지 않으면 사용자에게 이름을 묻고, username.json 파일에 저장한 후 기억하겠다는 메시지를 출력한다.


print("\n")
# 리팩토링(Refactoring)
# 코드가 잘 동작한다면, 특정 작업만 수행하는 여러 함수로 나누는 과정이 필요하다.

# 첫 번째, 함수로 만들기
# import json


def greet_user():
    """사용자를 이름으로 환영합니다."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name?: ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()


# 두 번째, 다른 함수로 분리하기
# import json


def get_stored_username():
    """저장된 사용자 이름이 있다면 불러옵니다."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None  # username.json 파일이 존재하지 않으면 None을 반환
    else:
        return username  # 저장된 사용자 이름을 반환

# ※ 함수는 예상하는 값을 반환하거나, 그렇지 않다면 None을 반환하게 만들어야 합니다.


def greet_user():
    """사용자를 이름으로 환영합니다."""
    username = get_stored_username()  # get_stored_username 함수의 리턴값을 변수에 저장
    if username:
        # 리턴값(사용자 이름)이 존재하면 환영 메시지를 출력
        print("Welcome back, " + username + "!")
    else:
        # 리턴값이 None 이면 새 사용자에게 이름을 묻고 저장
        username = input("What is your name?: ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("We'll remember you when you come back, " + username + "!")

greet_user()


# 세 번째, 한 번 더 분리! (각 함수가 단 하나의 목적만 가질 때까지~)
# import json


def get_stored_username():
    """저장된 사용자 이름이 있다면 불러옵니다."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None  # username.json 파일이 존재하지 않으면 None을 반환
    else:
        return username  # 저장된 사용자 이름을 반환

# ※ 함수는 예상하는 값을 반환하거나, 그렇지 않다면 None을 반환하게 만들어야 합니다.


def get_new_username():
    """새 사용자 이름을 묻고 파일에 저장합니다."""
    username = input("What is your name?: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username  # 저장한 새 사용자의 이름을 반환


def greet_user():
    """사용자를 이름으로 환영합니다."""
    username = get_stored_username()  # get_stored_username 함수의 리턴값을 변수에 저장
    if username:
        # 리턴값(사용자 이름)이 존재하면 환영 메시지를 출력
        print("Welcome back, " + username + "!")
    else:
        # 리턴값이 None 이면 새 사용자에게 이름을 묻고 저장
        username = get_new_username()  # get_new_username 함수의 리턴값을 변수에 저장
        print("We'll remember you when you come back, " + username + "!")

greet_user()

# ※ 리팩토링이 완료된 버전에서는 각 함수가 단 하나의 명확한 목적만 있습니다.
# 이렇게 작업을 구분해야 관리하고 확장하기 쉬운 명확한 코드를 만들 수 있습니다.

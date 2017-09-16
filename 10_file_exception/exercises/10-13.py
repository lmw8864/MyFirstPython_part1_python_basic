# 10-13.py

"""
10-13. 사용자 확인
"""

import json


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
        # 사용자 이름이 맞는지 체크
        check = input("Is your name " + username + "? (yes/no): ")
        if check == 'yes':
            print("Welcome back, " + username + "!")
        elif check == 'no':
            username = get_new_username()  # 사용자 이름이 아니면  새 사용자의 이름을 묻고 저장
            print("We'll remember you when you come back, " + username + "!")
        else:
            print("You have entered incorrectly.")
    else:
        # 리턴값이 None 이면 새 사용자에게 이름을 묻고 저장
        username = get_new_username()  # get_new_username 함수의 리턴값을 변수에 저장
        print("We'll remember you when you come back, " + username + "!")

greet_user()

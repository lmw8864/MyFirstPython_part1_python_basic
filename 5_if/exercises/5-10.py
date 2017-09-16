# 5-10.py

"""
5-10. 사용자 이름 체크
"""

current_users = ['Dongjin', 'Rancho', 'Jongwook', 'Minwoo', 'Guest']
new_users = ['GUEST', 'rancho', 'jiho', 'Yul', 'hyungrae']

for user in new_users:
    if user.title() in current_users:
        print("이미 사용중인 이름입니다. 다른 이름을 입력하세요.")
    else:
        print("사용 가능한 이름입니다.")


print('\n')
current_users_lower = [user.lower() for user in current_users]
# print(current_users_lower)

for user in new_users:
    if user.lower() in current_users_lower:
        print("이미 사용중인 이름입니다. 다른 이름을 입력하세요.")
    else:
        print("사용 가능한 이름입니다.")

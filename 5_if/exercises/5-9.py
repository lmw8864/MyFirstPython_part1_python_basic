# 5-9.py

"""
5-9. 사용자 없음
"""

# users = ['Dongjin', 'Rancho', 'Jongwook', 'admin-Minwoo', 'guest']
users = []

if users:
    for user in users:
        if user == 'admin-Minwoo':
            print("관리자님, 안녕하세요. 상태 보고서를 보시겠습니까?")
        else:
            print(user + "님, 안녕하세요. 로그인 해주셔서 감사합니다.")
else:
    print("사용자가 있어야 합니다.")
# 5-8.py

"""
5-8. 관리자에게 인사
"""

users = ['Dongjin', 'Rancho', 'Jongwook', 'admin-Minwoo', 'guest']
for user in users:
    if user == 'admin-Minwoo':
        print("관리자님, 안녕하세요. 상태 보고서를 보시겠습니까?")
    else:
        print(user + "님, 안녕하세요. 로그인 해주셔서 감사합니다.")

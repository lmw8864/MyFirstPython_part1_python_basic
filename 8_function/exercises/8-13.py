# 8-13.py

"""
8-13. 사용자 프로필
"""


def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
    profile = {}
    profile['first'] = first.title()
    profile['last'] = last.title()
    for key, value in user_info.items():
        profile[key] = str(value).title()
    return profile

user_profile = build_profile('minwoo', 'lee', location='seoul', field='python', age=33)
print(user_profile)

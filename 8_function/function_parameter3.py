# function_parameter3.py

"""
임의의 키워드 매개변수 사용하기

    임의의 숫자만큼 매개변수를 써야 하지만, 어떤 종류의 정보가 함수에 제공될지 미리 알 수 없을 때

    매개변수 앞에 '**' 를 붙여주면 파이썬이 매개변수명의 빈 딕셔너리를 만들고
    키-값 쌍을 받아서 이 딕셔너리에 저장한다.

     - 매개변수명로 **user_info 를 지정하면
            → 파이썬이 빈 딕셔너리 user_info 를 만들고 키-값 쌍을 받아서 저장함.
"""


def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# {'first': 'albert', 'last': 'einstein', 'field': 'physics', 'location': 'princeton'}

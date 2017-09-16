# 8-5.py

"""
8-5. 도시
"""

def describe_city(city_name, country_name='대한민국'):
    """도시와 나라를 출력합니다."""
    print(city_name.title() + "는 " + country_name.title() + "에 있습니다.")

describe_city('서울')
describe_city('인천')
describe_city(city_name='paris', country_name='france')

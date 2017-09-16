# class_5_collections_OrderedDict.py
"""
파이썬 표준 라이브러리에 포함되어 있는 collections 모듈의 OrderedDict 클래스를 살펴보자.

    - 딕셔너리는 키-값 쌍의 순서를 유지하지 못 한다.

    - collections 모듈의 OrderedDict 클래스의 인스턴스를 사용하면
     딕셔너리처럼 동작하면서 키-값 쌍의 순서도 유지할 수 있다.

"""
from collections import OrderedDict

favorite_languages = OrderedDict()  # 딕셔너리 {} 대신 OrderedDict 클래스의 인스턴스 사용

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Edward's favorite language is Ruby.
# Phil's favorite language is Python.

# ※ 다시 실행해도 순서가 바뀌지 않는다.

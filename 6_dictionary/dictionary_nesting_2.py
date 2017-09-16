# dictionary_nesting_2.py

"""
2. 딕셔너리 안에 리스트 담기
"""

# 딕셔너리 안에 리스트 담기

# 주문받은 피자에 관한 정보를 저장
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# 주문을 요약
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# You ordered a thick-crust pizza with the following toppings:
# 	mushrooms
# 	extra cheese

# ※ 딕셔너리의 키에 하나의 값 이상을 연결해야 한다면 언제든 리스트를 딕셔너리 안에 중첩해 쓸 수 있다.


# 딕셔너리 for 루프 안에서 다시 리스트 for 루프를 실행하는 예제
favorinte_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorinte_languages.items():  # items() 메소드 빼먹지 말자!
    if len(languages) == 1:
        print("\n" + name.title() + "`s favorite language is:")
    else:
        print("\n" + name.title() + "`s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# Sarah`s favorite language is:
# 	C
#
# Edward`s favorite languages are:
# 	Ruby
# 	Go
#
# Jen`s favorite languages are:
# 	Python
# 	Ruby
#
# Phil`s favorite languages are:
# 	Python
# 	Haskell

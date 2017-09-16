# dictionary_loop.py

# 키-값 쌍 전체에 루프 실행하기
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'lsast': 'fermi',
}
# items() 메서드는 키-값 쌍 리스트를 반환
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
# Key: first
# Value: enrico
#
# Key: username
# Value: efermi
#
# Key: lsast
# Value: fermi


# 코드를 더 읽기 쉽게~
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "`s favorite language is " + language.title() + ".")

# Sarah`s favorite language is C.
# Edward`s favorite language is Ruby.
# Phil`s favorite language is Python.
# Jen`s favorite language is Python.


print("\n")


# 딕셔너리의 모든 키(keys)에 루프 실행하기
# keys() 메서드는 키만 리스트로 반환
for name in favorite_languages.keys():
    print(name.title())
# Edward
# Sarah
# Phil
# Jen

# key() 메소드는 생략해도 돼요~ (딕셔너리에 루프를 실행하면 기본적으로 키에만 적용됨)
for name in favorite_languages:
    print(name.title())
# Edward
# Sarah
# Phil
# Jen

# ※ 명시적으로 keys() 메소드를 쓰는 편이 코드를 더 읽기 쉽게 만든다면 써주고,
# 그렇지 않다면 생략해도 된다. (난 쓰는게 좋아!)


print("\n")
# 루프 안에서 현재 키에 연결된 값에 접근하기
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + " I see your favorite language is " + favorite_languages[name].title() + "!")

# Phil
#  Hi Phil I see your favorite language is Python!
# Jen
# Sarah
#  Hi Sarah I see your favorite language is C!
# Edward


print("\n")

# 딕셔너리 키에 순서대로 루프 실행하기
# for 루프에서 반환하는 키를 sorted() 함수를 써서 정렬
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for taking the poll.")

# Edward thank you for taking the poll.
# Jen thank you for taking the poll.
# Phil thank you for taking the poll.
# Sarah thank you for taking the poll.


print("\n")


# 딕셔너리의 모든 값(values)에 루프 실행하기
# values() 메서드는 값만 리스트로 반환
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
# The following languages have been mentioned:
# C
# Ruby
# Python
# Python    # ※ 반복된 값이 존재함.


# 반복 없는 리스트를 얻으려면 set() 함수를 사용하자.
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())
# The following languages have been mentioned:
# C
# Ruby
# Python

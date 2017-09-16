# function_return.py


# formatted_name.py
def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환합니다."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Jimi Hendrix


# 매개변수를 옵션으로 만들기
# 매개변수에 기본값을 쓰면 옵션으로 만들 수 있음
def get_formatted_name(first_name, last_name, middle_name=''):  # 기본값으로 빈 문자열 지정하고 매개변수 리스트의 맨 뒤로 옮김
    """읽기 쉬운 전체 이름을 반환합니다."""
    if middle_name:  # 중간 이름이 있으면,
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Jimi Hendrix

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)  # John Lee Hooker


# 딕셔너리 반환하기
# person.py
def build_person(first_name, last_name):
    """사람에 관한 정보 딕셔너리를 반환합니다."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)  # {'first': 'jimi', 'last': 'hendrix'}


def build_person(first_name, last_name, age=''):
    """사람에 관한 정보 딕셔너리를 반환합니다."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)  # {'first': 'jimi', 'last': 'hendrix', 'age': 27}


# 함수에서 while 루프 사용하기
def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환합니다."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name.")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# Please tell me your name.
# (enter 'q' at any time to quit)
# First name: minwoo
# Last name: lee
#
# Hello, Minwoo Lee!
#
# Please tell me your name.
# (enter 'q' at any time to quit)
# First name: q

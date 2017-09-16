# dictionary_nesting_3.py

"""
3. 딕셔너리 안에 딕셔너리 담기
    (※주의: 코드가 복잡해지기 쉽다.)
"""

# 딕셔너리 안에 딕셔너리 담기
users = {
    'a_einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'm_curie': {
        'first': 'maria',
        'last': 'curie',
        'location': 'paris',
    }
}

for usename, user_info in users.items():
    print("\nUsername: " + usename)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# Username: a_einstein
# 	Full name: Albert Einstein
# 	Location: Princeton
#
# Username: m_curie
# 	Full name: Maria Curia
# 	Location: Paris

# ※ 각 사용자의 딕셔너리 구조는 완전히 같다.
# 필수는 아니지만, 딕셔너리를 중첩할 때는 이렇게 똑같은 구조를 써야 다루기 쉽다.

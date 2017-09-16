# 3-8.py

"""
3-8. 세계 둘러보기
"""
wishList_country = ['Canada', 'Spain', 'Indonesia', 'Finland', 'Croatia']
print(wishList_country)                             # ['Canada', 'Spain', 'Indonesia', 'Finland', 'Croatia']
# 리스트는 수정하지 않고 알파벳 순서로 출력
print(sorted(wishList_country))                     # ['Canada', 'Croatia', 'Finland', 'Indonesia', 'Spain']
# 리스트는 여전히 원래 순서
print(wishList_country)                             # ['Canada', 'Spain', 'Indonesia', 'Finland', 'Croatia']
# 리스트는 수정하지 않고 알파벳 역순으로 출력
print(sorted(wishList_country, reverse=True))       # ['Spain', 'Indonesia', 'Finland', 'Croatia', 'Canada']
# 리스트를 현재 순서의 반대로 정렬
wishList_country.reverse()
# 리스트의 순서가 바뀐 것을 확인
print(wishList_country)                             # ['Croatia', 'Finland', 'Indonesia', 'Spain', 'Canada']
# 리스트를 다시 반대로 정렬
wishList_country.reverse()
# 리스트 순서가 원래대로 돌아온 것을 확인
print(wishList_country)                             # ['Canada', 'Spain', 'Indonesia', 'Finland', 'Croatia']
# 리스트를 알파벳 순서로 정렬
wishList_country.sort()
# 리스트의 순서가 바뀐 것을 확인
print(wishList_country)                             # ['Canada', 'Croatia', 'Finland', 'Indonesia', 'Spain']
# 리스트를 알파벳 역순으로 정렬
wishList_country.sort(reverse=True)
# 리스트의 순서가 바뀐 것을 확인
print(wishList_country)                             # ['Spain', 'Indonesia', 'Finland', 'Croatia', 'Canada']

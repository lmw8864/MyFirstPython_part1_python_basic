# list-3.py
# 리스트 정리하기

# sort() 메서드로 리스트 영구 정렬하기

# 알파벳 순서로 정렬
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)                     # ['audi', 'bmw', 'subaru', 'toyota']
# 알파벳 반대 순서로 정렬
cars.sort(reverse=True)
print(cars)                     # ['toyota', 'subaru', 'bmw', 'audi']

# sorted() 함수로 리스트 임시 정렬하기 (※리스트의 실제 순서는 바뀌지 않음)
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("original list: ")        # original list:
print(cars)                     # ['bmw', 'audi', 'toyota', 'subaru']

print("sorted list: ")        # sorted list:
print(sorted(cars))             # ['audi', 'bmw', 'subaru', 'toyota']

print("original list again: ")   # original list again:
print(cars)                     # ['bmw', 'audi', 'toyota', 'subaru']


# reverse() 메서드를 사용하여 리스트 역순으로 바꾸기 (※알파벳 순서와 상관없이 현재 순서의 반대로만 정렬)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)                     # ['subaru', 'toyota', 'audi', 'bmw']

# len() 함수로 리스트 길이 구하기
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))                # 4

# 여태까지 메서드와 함수가 같은 것인 줄 알았는데, 이제보니 사용법이 다르다.
# sort(), reverse() ‘메서드’ → 리스트명.메서드
# sorted(), len() ‘함수’ → 함수(리스트명)

# list-1_2.py

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)                     # ['trek', 'cannondale', 'redline', 'specialized']

# 리스트 항목에 접근하기 (index)
print(bicycles[0])                  # trek

# 리스트 항목에 문자열 메서드 적용
print(bicycles[0].title())          # Trek

# 인덱스 위치는 0에서 시작
print(bicycles[1])                  # cannondale
print(bicycles[3])                  # specialized

# 마지막 항목에 접근하기
print(bicycles[-1])                 # specialized
print(bicycles[-2])                 # redline

# 리스트에서 개개의 값 사용
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)                      # My first bicycle was a Trek.

print('\n' + '#'*30)                ##############################
# 항목 변경, 추가, 제거

# 리스트 항목 수정하기
motorcycles = ['honda', 'yamaha', 'suzuki']     # ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles[0])               # ducati

# 리스트에 항목 추가하기

# append() 로 리스트 끝에 항목 추가하기
motorcycles = ['honda', 'yamaha', 'suzuki']     # ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')  # 리스트명.append('값')
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki']

# insert() 로 리스트에 항목 삽입하기 // insert() 메서드를 사용해 새 항목을 리스트 중간에 삽입할 수 있다.
motorcycles = ['honda', 'yamaha', 'suzuki']     # ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')  # 리스트명.insert(인덱스, 값)
print(motorcycles)                              # ['ducati', 'honda', 'yamaha', 'suzuki']


# 리스트에서 항목 제거

# del 문으로 항목 제거하기 // 제거할 항목의 위치를 알고 있다면 del 문을 쓸 수 있다.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki']

del motorcycles[0]  # del 리스트명[제거할 항목의 인덱스]
print(motorcycles)                              # ['yamaha', 'suzuki']


# pop() 으로 마지막 항목 꺼내서 사용하기 (꺼낸 항목은 리스트에서 제거됨)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki']

popped_motorcycles = motorcycles.pop()          # 'suzuki'가 리스트에서 제거되고 popped_motorcycles 변수에 저장되었다.
print(motorcycles)                              # ['honda', 'yamaha']
print(popped_motorcycles)                       # suzuki

# pop() 은 이런식으로~
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")  # The last motorcycle I owned was a Suzuki.


# pop(인덱스) 로 지정 항목 꺼내기 (꺼낸 항목은 리스트에서 제거됨)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")  # The first motorcycle I owned was a Honda.

# ※ 항목을 리스트에서 제거하고 닷 쓸 일이 없다면? -> del 문
# ※ 항목을 리스트에서 제거하고 어딘가에 사용할 거라면? -> pop(), pop(인덱스)


# 값으로 항목 제거하기 (제거할 값의 위치를 모를 때는 remove() 를~)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki']

# remove() 로 제거한 값은 pop() 처럼 사용이 가능 (책 버전)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki']
print("\nA " + too_expensive.title() + " is too expensive for me.")  # A Ducati is too expensive for me.

# ※주의: 리스트에 같은 값이 여러 개 있다면 remove() 메서드는 첫 번째 항목만 제거한다.
#  값을 전부 제거하고 싶으면 루프를 써야 함.

# remove() 로 제거한 값은 pop() 처럼 사용할 수 없음.(※주의)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki', 'ducati']

too_expensive = motorcycles.remove('ducati')
print(too_expensive)                          # None

# 리스트에 같은 값이 여러 개 있다면 remove() 메서드는 첫 번째 항목만 제거한다.
motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)                              # ['ducati', 'honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles)                              # ['honda', 'yamaha', 'suzuki', 'ducati']

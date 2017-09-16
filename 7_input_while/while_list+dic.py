# while_list+dic.py

# 리스트 항목을 다른 리스트로 옮기기

unconfirmed_users = ['alice', 'brian', 'Candace']  # 확인해야 하는 사용자 리스트
confirmed_users = []  # 확인된 사용자를 저장할 빈 리스트

while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # pop() 메서드로 리스트의 마지막 항목을 꺼내서 변수에 저장

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)  # append() 메서드를 이용, 변수에 저장된 항목을 다른 리스트에 추가

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice
#
# The following users have been confirmed:
# Candace
# Brian
# Alice


# 리스트에서 특정 값 모두 제거하기
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']  # 중복된 값들이 존재하는 리스트
print(pets)  # ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# 리스트에 항목이 존재하지 않을 때까지 제거 반복
while 'cat' in pets:
    pets.remove('cat')

print(pets)  # ['dog', 'dog', 'goldfish', 'rabbit']


# 사용자가 입력한 값으로 딕셔너리 채우기

# mountain_poll.py
responses = {}  # 빈 딕셔너리 정의

polling_active = True  # 플래그

while polling_active:
    # 이름과 응답을 묻는다
    name = input("\nWhat is your name? : ")
    response = input("\nWhich mountain would you like to climb someday? : ")

    # 응답을 딕셔너리에 저장
    responses[name] = response

    # 다른 사람도 설문에 참여할지 묻는다
    repeat = input("Would you like to let another person respond? (yes / no): ")
    # 루프 탈출 조건
    if repeat == 'no':
        polling_active = False

# 설문 끝, 결과를 출력
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

# What is your name? : 홍길동
#
# Which mountain would you like to climb someday? : 금강산
# Would you like to let another person respond? (yes / no): yes
#
# What is your name? : 신동진
#
# Which mountain would you like to climb someday? : 계양산
# Would you like to let another person respond? (yes / no): yes
#
# What is your name? : 이민우
#
# Which mountain would you like to climb someday? : 안산
# Would you like to let another person respond? (yes / no): no
#
# --- Poll Result ---
# 신동진 would like to climb 계양산.
# 이민우 would like to climb 안산.
# 홍길동 would like to climb 금강산.

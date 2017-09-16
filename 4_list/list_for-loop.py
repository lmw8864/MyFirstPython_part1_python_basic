# list_for-loop.py

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# alice
# david
# carolina

# ※ 임시변수는 아무 이름이나 쓸 수 있지만,
#  이왕이면 리스트(magicians, 복수) 중 단 하나(magician, 단수)라는 의미처럼 쓰는 게 좋다.

# 루프 안에서 더 많은 일 하기
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.
#
# David, that was a great trick!
# I can't wait to see your next trick, David.
#
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
#

# for 루프부터 루프의 마지막 행까지를 루프 블록이라고 한다.

# for 루프 다음에 어떤 일 하기
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.
#
# David, that was a great trick!
# I can't wait to see your next trick, David.
#
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
#
# Thank you, everyone. That was a great magic show!

print("\n")

# 들여쓰기 에러 피하기

# 들여쓰기 자체를 잊었을 때
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
# print(magician)  # 들여쓰기 에러
    pass

#   File "D:/Users/Minwoo_Lee/Documents/ImaDeveloper/myFirstPython/part1/4_list/list_for-loop.py", line 54
#     print(magician)
#         ^
# IndentationError: expected an indented


# 추가 행을 들여쓰지 않았을 때
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")  # 논리적 에러(logical error)

# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.


# 불필요한 들여쓰기를 했을 때
message = "Hello Python world!"
    # print(message)  # 불필요한 들여쓰기

#   File "D:/Users/Minwoo_Lee/Documents/ImaDeveloper/myFirstPython/part1/4_list/list_for-loop.py", line 74
#     print(message)
#     ^
# IndentationError: unexpected indent


# 루프 다음에 불필요한 들여쓰기를 했을 때
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you, everyone. That was a great magic show!")  # 불필요한 들여쓰기(논리적 에러)

# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.
#
# Thank you, everyone. That was a great magic show!
# David, that was a great trick!
# I can't wait to see your next trick, David.
#
# Thank you, everyone. That was a great magic show!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
#
# Thank you, everyone. That was a great magic show!


# 콜론(:)을 잊었을 때
magicians = ['alice', 'david', 'carolina']
# for magician in magicians  # 콜론(:)을 빼먹음
#     print(magician)

#   File "D:/Users/Minwoo_Lee/Documents/ImaDeveloper/myFirstPython/part1/4_list/list_for-loop.py", line 109
#     for magician in magicians
#                             ^
# SyntaxError: invalid syntax

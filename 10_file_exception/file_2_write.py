# file_2_write.py

"""
파일에 쓰기

    - 파일에 쓰려면 open() 함수의 두 번째 매개변수에 open 모드를 지정해주어야 합니다.

    - open 모드:
        - 읽기(read) 모드: 'r'
        - 쓰기(write) 모드: 'w'
        - 이어붙이기(append) 모드: 'a'
        - 읽고 쓰기 모드: 'r+'

    ※ 두 번째 매개변수 생략 시 기본적으로 읽기 모드로 오픈
    ※ 쓰기 모드로 오픈 시 파일이 존재하지 않으면 자동으로 만듭니다.
     해당 파일이 이미 존재할 경우에는 파일 객체를 반환하기 전에 기존 파일을 지우므로 조심해야 합니다.
    ※ 파이썬은 텍스트 파일에 문자열만 쓸 수 있습니다. (숫자 데이터를 쓰려면 str() 함수 이용)
"""

# 빈 파일에 쓰기
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# programming.txt 내용:
# I love programming.


print("\n")
# 여러 행 쓰기
# write() 함수는 텍스트에 줄바꿈 문자를 추가하지 않습니다.
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

# programming.txt 내용:
# I love programming.I love creating new games.

# --> 행을 분리하려면 write() 문에 줄바꿈 문자(\n)을 넣어주어야 합니다.
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# programming.txt 내용:
# I love programming.
# I love creating new games.


print("\n")
# 파일에 이어붙이기
# 기존의 내용에 덮어쓰지 않고 파일에 내용을 추가하려면 이어붙이기 모드로 열 수 있습니다.
# 파일에 쓰는 행은 모두 파일 마지막에 추가
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I also love finding meaning in large datasets.\n")

# programming.txt 내용:
# I love programming.
# I love creating new games.
# I also love finding meaning in large datasets.
# I also love finding meaning in large datasets.

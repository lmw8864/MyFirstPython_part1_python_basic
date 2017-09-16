# try-except_FileNotFoundError.py

"""
1. FileNotFoundError 예외 처리
    - 파일로 작업할 때 흔히 일어나는 문제는 파일이 없는 문제

2. 텍스트 분석

3. 여러 파일 다루기

4. 조용히 실패하기
"""

# 존재하지 않는 파일을 읽으려 할 때
# filename = 'alice.txt'
#
# with open(filename) as f:
#     contents = f.read()

# Traceback (most recent call last):
#   File "D:/Users/Minwoo_Lee/Documents/ImaDeveloper/myFirstPython/part1/10_file_exception/try-except_FileNotFoundError.py", line 12, in <module>
#     with open(filename) as f:
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'


# try-except 블록 (FileNotFoundError 예외 처리)
filename = 'alice.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# Sorry, the file alice.txt does not exist.


# 텍스트 분석

# 단어 리스트를 만드는 split() 메서드
# split() 메서드: 공백을 기준으로 문자열을 분리하고 각 부분을 리스트에 저장
title = "Alice in Wonderland"
print(title.split())
# ['Alice', 'in', 'Wonderland']

# 파일에 들어 있는 단어 수 세기
filename = 'alice.txt'

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 파일에 들어있는 단어를 셉니다.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

# The file alice.txt has about 29461 words.


print("\n")


# 여러 파일 다루기
# 앞의 프로그램을 함수로 만들기
def count_words(filename):
    """파일에 들어있는 단어를 셉니다."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 파일에 들어 있는 단어를 셉니다.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)  # The file alice.txt has about 29461 words.


print("\n")
# 분석할 파일 리스트를 작성해서 루프로 호출하기
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# The file alice.txt has about 29461 words.
# Sorry, the file siddhartha.txt does not exist.  --> 에러가 일어나도 텍스트 분석을 계속할 수 있다.
# The file moby_dick.txt has about 215136 words.
# The file little_women.txt has about 189079 words.


print("\n")


# 조용히 실패하기
# 사용자에게 모든 예외를 보고할 필요는 없습니다.
def count_words(filename):
    """파일에 들어있는 단어를 셉니다."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # FileNotFoundError가 일어나면 아무 일도 하지 않음.
    else:
        # 파일에 들어 있는 단어를 셉니다.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# The file alice.txt has about 29461 words.
# The file moby_dick.txt has about 215136 words.
# The file little_women.txt has about 189079 words.


# 어떤 에러를 보고할지 정하기
# 사용자에게 에러를 보고할지, 아니면 조용히 실패할지 판단
# 사용자가 원하지 않는 정보를 제공하면 프로그램의 사용성이 떨어질 수 있습니다.

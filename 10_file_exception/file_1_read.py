# file_1_read.py

"""
파일에서 읽기

    - 파일 전체 읽기
    - 한 행씩 읽기
    - 파일에서 행 리스트 만들기
    - 파일 콘텐츠 다루기
    - 백만 단위의 큰 숫자 다루기
    - 콘텐츠 분석

※ 파일 경로
    상대 경로:
        - 리눅스 또는 macOS: with open('text_files/filename.txt') as file_object:
        - 윈도우: 슬래시(/) 대신 역슬래시(\) 사용

    절대 경로: (상대 경로가 동작하지 않을 때 쓰면 된다.)
        - 리눅스 또는 macOS:
            file_path = '/home/dev/other_files/text_files/filename.txt'
            with open(file_path) as file_object:


    # pi_digits.txt

    3.1415926535
      8979323846
      2643383279

"""

# 파일 전체 읽기
with open('pi_digits.txt') as file_object:  # open() 함수는 pi_digits.txt 파일을 나타내는 객체를 반환, file_object 에 저장
    contents = file_object.read()  # read() 메서드는 파일 콘텐츠 전체를 읽고 문자열 형태로 contents 에 저장
    print(contents)  # contents 출력

    # 3.1415926535
    # 8979323846
    # 2643383279
    # (빈 행)

    print(contents.rstrip())  # 빈 행(오른쪽 공백) 제거

    # 3.1415926535
    #   8979323846
    #   2643383279

# ※ with 문을 쓰면 open()이 반환한 파일 객체는 with 블록 안에서만 쓸 수 있다.


print("\n")
# 한 행씩 읽기
# 파일에 들어있는 정보를 찾거나, 파일에 들어있는 텍스트를 수정해야 하는 때 등
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:  # file_object 는 반복 가능한 객체
        print(line)

        # 3.1415926535
        #
        # 8979323846
        #
        # 2643383279


with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())  # 빈 행 제거

        # 3.1415926535
        # 8979323846
        # 2643383279


print("\n")
# 파일에서 행 리스트 만들기
# with 문을 쓰면 open()이 반환한 파일 객체는 with 블록 안에서만 쓸 수 있다.
# with 블록 밖에서도 파일 콘텐츠에 접근하려면?
# with 블록 안에서 파일 행들을 리스트에 저장하고, 그 리스트로 블록 밖에서 작업하면 된다.
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  # 한 행씩 읽어 리스트에 저장

# 블록 밖으로 나와서도 저장한 리스트를 이용해서 작업할 수 있다.
for line in lines:
    print(line.rstrip())

    # 3.1415926535
    # 8979323846
    # 2643383279


print("\n")
# 파일 콘텐츠 다루기
# 파일에 들어있는 숫자를 공백없이 단 하나의 문자열로 만들어 보자.
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''  # 파이(pi)의 숫자를 저장할 빈 문자열 정의
for line in lines:
    pi_string += line.rstrip()  # 각 행의 줄바꿈문자 제거 후 pi_string 변수에 문자열 추가

print(pi_string)  # 3.1415926535  8979323846  2643383279
print(len(pi_string))  # 36


pi_string = ''  # 파이(pi)의 숫자를 저장할 빈 문자열 정의
for line in lines:
    pi_string += line.strip()  # 각 행의 공백을 모두 제거 후 pi_string 변수에 문자열 추가

print(pi_string)  # 3.141592653589793238462643383279
print(len(pi_string))  # 32


print("\n")
# 백만 단위의 큰 숫자 다루기
# 소수점 아래 50자리만 출력
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")  # 3.14159265358979323846264338327950288419716939937510...
print(len(pi_string))  # 1000002


print("\n")
# 간단한 분석
# 누군가의 생일이 파이(pi)의 첫 번째 백만 자리 안에 들어 있는지 알아봅시다.
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form MMDDYY: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("your birthday does not appears in the first million digits of pi.")

# Enter your birthday, in the form MMDDYY: 851231
# Your birthday appears in the first million digits of pi!

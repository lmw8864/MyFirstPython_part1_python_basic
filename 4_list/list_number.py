# list_number.py

# range() 함수 사용하기
for value in range(1, 5):
    print(value)
print("\n")
# 1
# 2
# 3
# 4

# range(시작숫자, 끝숫자) 에서 끝숫자는 포함되지 않는다.
# range() 함수는 '시작숫자'에서 시작해 '끝숫자'에 도달하면 멈추기 때문


# range() 함수로 숫자 리스트 만들기
numbers = list(range(1, 6))  # list() 함수로 감싸면 리스트를 만들 수 있다.
print(numbers)  # [1, 2, 3, 4, 5]


# 1~10 짝수 리스트 만들기
even_numbers = list(range(2, 11, 2))  # range(시작숫자, 끝숫자, 증가치)
print(even_numbers)  # [2, 4, 6, 8, 10]


# 1~10 제곱수 리스트 만들기
squares = []  # 빈 리스트 생성
for value in range(1, 11):
    square = value**2
    squares.append(square)  # 리스트의 마지막에 항목 추가하기

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 코드를 좀 더 간결하게!
squares = []
for value in range(1, 11):
    squares.append(value**2)  # 임시변수 생략하고 바로 넣기

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 때로는 임시변수가 코드를 읽기 쉽게 하지만, 코드가 길어지는 원인이 되기도 합니다.
# 우선 코드를 이해하기 쉽게 만드는 데 주력하세요. 그리고 다음에 코드를 다시 살펴볼 때는 좀 더 효율적인 방법을 택하세요.

print("\n")

# 숫자 리스트를 이용한 단순한 통계
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # digits = list(range(0, 10))
print(min(digits))  # 0
print(max(digits))  # 9
print(sum(digits))  # 45

print("\n")

# 리스트 내포 (list comprehension) ★ # 짱짱!
squares = [value**2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 1. 의미있는 리스트 이름으로 시작
# 2. [ 열고,
# 3. 새 리스트에 저장할 값을 만들 표현식을 정의
# 4. 표현식에 제공할 값을 생성하는 for 루프
# 5. ] 닫으면 끝.

# (※ for문 마지막에 콜론(:) 없어요~)

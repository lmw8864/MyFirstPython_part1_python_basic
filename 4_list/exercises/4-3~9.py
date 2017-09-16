# 4-3.py

"""
4-3. 20까지 세기
4-4. 백만
4-5. 백만까지 더하기
4-6. 홀수
4-7. 3배수
4-8. 세제곱
4-9, 세제곱 내포
"""
# 1~20 출력하기
for num in range(1, 21):
    print(num)
print("\n")

# 백만
# 1~백만까지 숫자리스트를 만들고 출력하기
numbers = list(range(1, 1000001))
for number in numbers:
    print(number)
print("\n")

# 백만까지 더하기
numbers = list(range(1, 1000001))
# 리스트의 시작과 끝 출력
print(min(numbers))
print(max(numbers))
# 백만까지의 합 구하기
print(sum(numbers))
print("\n")

# 1~20 홀수 리스트 만들고 출력하기
even_numbers = list(range(1, 21, 2))
for even_number in even_numbers:
    print(even_number)
print("\n")

# 3~30 3의 배수 리스트 만들고 출력하기
triple_numbers = list(range(3, 31, 3))
for triple_number in triple_numbers:
    print(triple_number)
print("\n")

# 1~10의 세제곱 리스트 만들고 출력하기
cube_numbers = []
for num in range(1, 11):
    cube_numbers.append(num**3)
print(cube_numbers)
print("\n")

# 리스트 내포(list comprehension)을 사용해서 1~10 세제곱 리스트 만들기
cube_numbers = [num**3 for num in range(1, 11)]
print(cube_numbers)

# while_continue.py

"""
continue 문을 쓰면 조건 테스트 결과에 따라 루프 처음으로 돌아갈 수 있다.
    - 특정 조건에 대해서만 건너뛰고 계속 반복하고 싶을 때 쓰면 유용할 듯.
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # 2, 4, 6, 8 이면 아래 코드 무시하고 처음으로 돌아감.

    print(current_number)

# 1
# 3
# 5
# 7
# 9

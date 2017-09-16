# 7-5.py

"""
7-5. 영화 입장권
"""

total_price = 0
price_between_3_12 = 10
price_over12 = 15
while True:
    age = input("나이를 입력하세요.('end'를 입력하시면 종료됩니다): ")

    if age == 'end':
        break
    else:
        if int(age) < 3:
            print("3세 미만은 무료 관람 가능하세요.")
        elif int(age) < 13:
            print("3세 이상 12세 이하는 10달러입니다.")
            total_price += price_between_3_12
        else:
            print("13세 이상은 15달러입니다.")
            total_price += price_over12

print("총 가격은 " + str(total_price) + "달러입니다.")

# 나이를 입력하세요.('end'를 입력하시면 종료됩니다): 2
# 3세 미만은 무료 관람 가능하세요.
# 나이를 입력하세요.('end'를 입력하시면 종료됩니다): 5
# 3세 이상 12세 이하는 10달러입니다.
# 나이를 입력하세요.('end'를 입력하시면 종료됩니다): 12
# 3세 이상 12세 이하는 10달러입니다.
# 나이를 입력하세요.('end'를 입력하시면 종료됩니다): 15
# 13세 이상은 15달러입니다.
# 나이를 입력하세요.('end'를 입력하시면 종료됩니다): end
# 총 가격은 35달러입니다.

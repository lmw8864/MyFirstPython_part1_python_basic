# 7-6_1.py

"""
7-6. 세 가지 탈출구
"""

# while 문 조건 테스트로 루프 멈추기
total_price = 0
price_between_3_12 = 10
price_over12 = 15

age = " "  # 초깃값 지정
while age:
    age = input("나이를 입력하세요.('end'를 입력하시면 종료됩니다): ")
    if age == 'end':
        age = False
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

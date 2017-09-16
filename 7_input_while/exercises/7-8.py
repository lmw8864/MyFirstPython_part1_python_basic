# 7-8.py

"""
7-8. 제과점
"""

sandwich_orders = ['스파이시 이탈리안', '치킨 데리야끼', '터키 베이컨', '써브웨이 클럽', '터키 베이컨 아보카도']
sandwich_orders.reverse()  # pop() 하면 뒤부터 나오니까 역순으로 해봤다. 주문한 순서대로 나와야 되지 않겠니?
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(finished_sandwich + " 샌드위치를 만들었습니다.")

    finished_sandwiches.append(finished_sandwich)

print("\nFinishied sandwiches list:\n")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

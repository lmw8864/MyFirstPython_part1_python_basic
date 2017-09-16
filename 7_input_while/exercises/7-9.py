# 7-9.py

"""
7-9. 패스트라미 없음
"""

sandwich_orders = ['스파이시 이탈리안', 'pastrami', '치킨 데리야끼', '터키 베이컨',
                   'pastrami', '써브웨이 클럽', '터키 베이컨 아보카도', 'pastrami']
sandwich_orders.reverse()  # pop() 하면 뒤부터 나오니까 역순으로 해봤다. 주문한 순서대로 나와야 되지 않겠니?
finished_sandwiches = []

print("주문 리스트:")
for sandwich_order in sandwich_orders:
    print("\t" + sandwich_order.title())

print("\n죄송합니다. Pastrami 샌드위치가 다 떨어져서 주문 리스트에서 빠집니다.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(finished_sandwich + " 샌드위치를 만들었습니다.")

    finished_sandwiches.append(finished_sandwich)

print("\nFinishied sandwiches list:\n")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

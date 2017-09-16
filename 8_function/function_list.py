# function_list.py

# 리스트 전달 (리스트를 매개변수로 받을 수 있다.)
def greet_users(names):
    """리스트의 각 사용자에게 단순한 환영 인사를 출력합니다."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Hello, Hannah!
# Hello, Ty!
# Hello, Margot!


print("\n")
# 함수에서 리스트 수정하기

# 출력할 디자인으로 시작합니다.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트합니다.
# 출력한 각 디자인을 completed_models로 옮깁니다.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # 디자인에서 3D 출력 시뮬레이트
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 출력이 끝난 모델 모두 표시
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: iphone case
#
# The following models have been printed:
# dodecahedron
# robot pendant
# iphone case


print("\n")
# 위 코드를 함수 코드로 바꾸기

def print_models(unprinted_designs, completed_models):
    """
    남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트합니다.
    출력한 각 디자인을 completed_models로 옮깁니다.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 디자인에서 3D 출력 시뮬레이트
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """출력이 끝난 모델 모두 표시"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: iphone case
#
# The following models have been printed:
# dodecahedron
# robot pendant


# ※ 모든 함수가 특정한 작업 한 가지를 수행해야 한다.
#  함수가 너무 많은 작업을 한다고 생각하면 함수를 두 개로 나눠보자.
#  함수에서 다른 함수를 호출할 수 있으므로 복잡한 작업을 몇 단계로 쉽게 나눌 수 있다.

print("\n")
# 함수가 리스트를 수정하지 못하게 막기
# 위 코드에서 보면, 작업이 끝난 뒤 unprinted-designs 리스트에는 아무것도 남아있지 않다.
# 만약 작업이 끝난 뒤에도 원래 리스트를 그대로 보존하고 싶다면?
# 함수에 원래 리스트가 아니라 사본을 전달하는 방법을 사용한다. (사본 --> 슬라이스 표기법)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs, completed_models)
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print("\n")
print(unprinted_designs)  # ['iphone case', 'robot pendant', 'dodecahedron']
# 원래 리스트가 변경되지 않고 그대로 보존되어 있는 것을 확인

# ※ 리스트 사본을 함수에 전달해서 원래 내용을 보존할 수 있긴 하지만,
# 뚜렷한 이유가 없다면 원래 리스트를 함수에 전달해야 한다.
# 함수가 기존 리스트를 사용해야 리스트를 복사하는 시간과 메모리를 아낄 수 있으며,
# 특히 리스트가 클 때는 그 차이가 심하다.

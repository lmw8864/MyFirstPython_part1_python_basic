# 9-1.py

"""
9-1. 레스토랑
"""


class Restaurant():
    """레스토랑을 모델화"""
    def __init__(self, restaurant_name, cuisine_type):
        """속성 초기화"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # 메서드 정의
    def describe_restaurant(self):
        """레스토랑 정보를 출력합니다."""
        print("\n레스토랑 이름: " + self.restaurant_name.title())
        print("음식 타입: " + self.cuisine_type.title())

    def open_restaurant(self):
        """레스토랑 오픈 메시지 출력"""
        print("\n" + self.restaurant_name + "이 오픈했습니다. 많은 관심 부탁드립니다!")


# 인스턴스 생성
mad_for_garlic = Restaurant('mad for garlic', 'italian')
papas_dining = Restaurant("papa's dining", 'japanese')

# 각 인스턴스의 속성 출력
print(mad_for_garlic.restaurant_name + ", " + mad_for_garlic.cuisine_type)
print(papas_dining.restaurant_name + ", " + papas_dining.cuisine_type)

# 각 인스턴스의 메서드 호출
mad_for_garlic.describe_restaurant()
mad_for_garlic.open_restaurant()

papas_dining.describe_restaurant()
papas_dining.open_restaurant()

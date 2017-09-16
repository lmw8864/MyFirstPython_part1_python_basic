# 9-6.py

"""
9-6. 아이스크림 가판대
"""


class Restaurant():
    """레스토랑을 모델화"""
    def __init__(self, restaurant_name, cuisine_type):
        """속성 초기화"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # 기본값 0

    def describe_restaurant(self):
        """레스토랑 정보를 출력합니다."""
        print("\n레스토랑 이름: " + self.restaurant_name.title())
        print("음식 타입: " + self.cuisine_type.title())

    def open_restaurant(self):
        """레스토랑 오픈 메시지 출력"""
        print("\n" + self.restaurant_name + "이 오픈했습니다. 많은 관심 부탁드립니다!")

    # 서빙한 고객 숫자를 지정하는 메서드 추가
    def set_number_served(self, number):
        """서빙한 고객 숫자를 지정합니다."""
        self.number_served = number

    # 서빙한 고객 숫자를 지정한 값만큼 늘리는 메서드 추가
    def increment_number_served(self, number):
        """서빙한 고객 숫자를 지정한 값만큼 늘립니다."""
        self.number_served += number


class IceCreamStand(Restaurant):
    """아이스크림 가판대"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        부모 클래스의 속성을 초기화하고
        아이스크림 맛 리스트를 저장하는 속성을 추가합니다.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['바닐라', '딸기', '메론', '체리', '바나나', '쿠키', '커피']
        self.flavors.sort()

    def show_flavors(self):
        """아이스크림 맛 리스트를 출력합니다."""
        print("\n아이스크림 맛 리스트: ")
        for flavor in self.flavors:
            print(" - " + flavor)

ice_house = IceCreamStand('아이스크림 잘하는 집', 'icecream')
ice_house.describe_restaurant()
ice_house.show_flavors()

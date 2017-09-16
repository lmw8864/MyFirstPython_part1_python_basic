# class_3_inheritance_1.py

"""
상속
    - 부모 클래스가 반드시 현재 파일에 있어야 하며, 반드시 자식 클래스보다 앞에 있어야 한다.
    - super() 함수
"""

# 부모 클래스
class Car():
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 기본값 0

    def get_descriptive_name(self):
        """알아보기 쉬운 이름 변환"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력합니다."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        주행거리 표시기를 주어진 값으로 바꿉니다.
        주행거리 표시기를 더 작은 값으로 바꾸려 하면 거부합니다.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행거리 표시기를 롤백할 수 없습니다.")

    def increment_odometer(self, miles):
        """주행거리를 주어진 양만큼 늘립니다."""
        self.odometer_reading += miles


# 자식 클래스
class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타냅니다."""

    def __init__(self, make, model, year):
        """부모 클래스의 속성을 초기화합니다."""
        super().__init__(make, model, year)  # ※ self 는 쓰지 않음


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# 2016 tesla model S


# 자식 클래스에 새 속성과 메서드 추가
class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타냅니다."""

    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화한 다음
        전기자동차에만 해당하는 속성을 초기화합니다.
        """
        super().__init__(make, model, year)  # ※ self 는 쓰지 않음
        self.battery_size = 70  # 자식클래스에만 해당하는 속성 추가

    # 자식클래스에만 해당하는 메서드 추가
    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())  # 2016 Tesla Model S
my_tesla.describe_battery()
# This car has a 70-kWh battery.


# 부모 클래스에서 상속한 메서드가 자식 클래스에서 모델화하려는 것과 맞지 않는다면 언제든지 오버라이드 할 수 있다.
# 오버라이드가 필요하다면 자식 클래스에 오버라이드할 메서드와 같은 이름의 메서드를 만들면 된다.

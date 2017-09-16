# class_3_inheritance_2_instance_attribute.py

"""
속성인 인스턴스

    - 클래스의 일부분을 분리할 수 있다.
    - 큰 클래스를 작은 클래스로 나눠서 함께 사용할 수 있다.
    - 다른 클래스의 인스턴스를 생성해서 속성으로 쓸 수 있다.
"""


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


# 별도의 Battery 클래스로 분리
class Battery():
    """전기자동차의 배터리를 모델화하려는 단순한 시도"""

    def __init__(self, battery_size=70):  # bettery_size 매개변수는 옵션이며 값이 제공되지 않으면 기본값 70을 갖는다.
        """배터리 속성 초기화"""
        self.battery_size = battery_size

    # ElectricCar 클래스에서 옮겨왔음.
    def describe_battery(self):
        """배터리 크기를 설명하는 문장을 출력합니다."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    # 배터리에 대한 메서드 추가
    def get_range(self):
        """이 배터리가 제공하는 주행 가능 거리를 출력합니다."""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타냅니다."""

    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화한 다음
        전기자동차에만 해당하는 속성을 초기화합니다.
        """
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()  # Battery 클래스의 인스턴스를 생성해서 self.battery 속성에 저장

    # def describe_battery(self):
    #     Battery 클래스로 옮김..


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())  # 2016 Tesla Model S
my_tesla.battery.describe_battery()
# This car has a 70-kWh battery.

my_tesla.battery.get_range()
# This car can go approximately 240 miles on a full charge.

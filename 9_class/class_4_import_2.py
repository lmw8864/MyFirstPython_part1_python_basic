from modules import car  # car.py 모듈 전체를 임포트

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# 2016 Volkswagen Beetle
# 2016 Tesla Roadster

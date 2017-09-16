# employee.py


class Employee():
    """직원의 이름과 성, 연봉을 받고 이들을 속성으로 저장합니다."""
    def __init__(self, first_name, last_name, annual_salary):
        self.full_name = first_name + last_name
        self.annual_salary = annual_salary
        self.employee = self.full_name + " " + str(self.annual_salary)

    def give_raise(self, increment=500):
        """연봉 증가"""
        self.annual_salary += increment

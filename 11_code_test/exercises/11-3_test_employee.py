# 11-3_test_employee.py

"""
11-3. 직원
"""
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Employee 클래스 테스트"""

    def setUp(self):
        """모든 테스트에서 사용할 새 직원 인스턴스를 생성합니다."""
        self.mwlee = Employee('minwoo', 'lee', 3000)  # 인스턴스 생성

    def test_give_default_raise(self):
        """기본 연봉 증가 테스트"""
        self.mwlee.give_raise()
        self.assertEqual(self.mwlee.annual_salary, 3500)

    def test_give_custom_raise(self):
        """커스텀 연봉 증가 테스트"""
        self.mwlee.give_raise(1000)
        self.assertEqual(self.mwlee.annual_salary, 4000)

if __name__ == "__main__":
    unittest.main()

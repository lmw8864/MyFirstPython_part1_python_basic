# test_survey.py

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """AnonymousSurvey 클래스 테스트"""

    def setUp(self):
        """모든 테스트에서 사용할 설문조사 인스턴스와 응답을 생성합니다."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)  # 인스턴스 생성
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """응답 하나가 제대로 저장되는지 테스트"""
        self.my_survey.store_response(self.responses[0])  # 응답으로 'English' 저장
        self.assertIn(self.responses[0], self.my_survey.responses)  # 응답 리스트에 'English'가 들어있는지 확인

    def test_store_three_responses(self):
        """응답 세 개가 제대로 저장되는지 테스트"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


# unittest.main()

if __name__ == "__main__":
    unittest.main()

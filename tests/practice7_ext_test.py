import unittest
from typing import Callable, Any, Dict

from hse_python.practice_7_ext.client import Client
from hse_python.practice_7_ext.server import IncomeCalculator


def mock_request_hour_income(answers: Dict[int, Dict[int, Dict[int, Dict[str, Any]]]])\
        -> Callable[[Any, int, int, int], Dict[str, Any]]:
    def wrapped(params: Dict[str, any]):
        return answers[params["year"]][params["month"]][params["salary"]]
    return wrapped


class ClientTestCase(unittest.TestCase):
    def __get_mocked_client(self):
        answers = {
            2022: {
                11: {
                    87000: {
                        "year": 2022,
                        "month": 11,
                        "salary": 87000,
                        "hour_income": 1208.33,
                    }
                }
            }
        }
        client = Client(server_url="")
        client.request_hour_income = mock_request_hour_income(answers)
        return client

    def test_hour_income_correctness(self):
        client = self.__get_mocked_client()

        result = client.get_hour_income(year=2022, month=11, salary=87000)
        self.assertEqual(1208.33, result)


def mock_make_request_to_isdayoff(answers: Dict[int, Dict[int, str]]) -> Callable[[Any, int, int], str]:
    def wrapped(year: int, month: int):
        return answers[year][month]
    return wrapped


class IncomeCalculatorTestCase(unittest.TestCase):
    def __get_mocked_income_calculator(self):
        income_calculator = IncomeCalculator()
        income_calculator.make_request_to_isdayoff = mock_make_request_to_isdayoff(
            {
                2022: {
                    10: "1111100111110011111001111100",  # 20 working days
                    11: "1111100111110011111001111",  # 19 working days
                }
            }
        )
        return income_calculator

    def test_hour_income_correctness(self):
        income_calculator = self.__get_mocked_income_calculator()

        result1 = income_calculator.get_hour_income(year=2022, month=11, salary=1000)
        self.assertEqual(6.58, result1)

        result2 = income_calculator.get_hour_income(year=2022, month=10, salary=1000)
        self.assertEqual(6.25, result2)

    def test_day_income_correctness(self):
        income_calculator = self.__get_mocked_income_calculator()

        result1 = income_calculator.get_day_income(year=2022, month=11, salary=1000)
        self.assertEqual(52.63, result1)

        result2 = income_calculator.get_day_income(year=2022, month=10, salary=1000)
        self.assertEqual(50, result2)


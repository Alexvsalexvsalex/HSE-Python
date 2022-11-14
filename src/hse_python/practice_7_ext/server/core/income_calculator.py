import logging

import requests

from .cache import WorkingDaysCache


logger = logging.getLogger(__name__)


class IncomeCalculator:
    def __init__(self):
        self.working_days_cache = WorkingDaysCache()

    def make_request_to_isdayoff(self, year: int, month: int) -> str:
        logger.info("Request working days from isdayoff")
        response = requests.get(
            "https://isdayoff.ru/api/getdata?year={}&month={:02d}".format(year, month)
        )
        logger.info(f"Response from isdayoff {response}")
        return response.text

    def get_working_days_from_isdayoff(self, year: int, month: int) -> int:
        result = self.make_request_to_isdayoff(year, month)
        return result.count("1")

    def get_working_days(self, year: int, month: int) -> int:
        logger.info("Request working days from local cache")
        cached_value = self.working_days_cache.get(year, month)
        if cached_value is None:
            correct_value = self.get_working_days_from_isdayoff(year, month)
            self.working_days_cache.update(year, month, correct_value)
            return correct_value
        else:
            return cached_value

    def get_hour_income(self, year: int, month: int, salary: int) -> float:
        days = self.get_working_days(year, month)
        return round(salary / days / 8, 2)

    def get_day_income(self, year: int, month: int, salary: int) -> float:
        days = self.get_working_days(year, month)
        return round(salary / days, 2)

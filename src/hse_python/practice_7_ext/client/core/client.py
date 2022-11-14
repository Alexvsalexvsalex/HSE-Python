import json

import requests

from .errors import ClientError


class Client:
    def __init__(self, server_url: str):
        self.server_url = server_url

    def request_hour_income(self, params):
        response = requests.get(f"{self.server_url}/calc_salary", params=params)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise ClientError(f"Response status code is {response.status_code}")

    def get_hour_income(self, year: int, month: int, salary: int) -> float:
        result = self.request_hour_income({"year": year, "month": month, "salary": salary})
        if "hour_income" in result:
            return result.get("hour_income")
        else:
            raise ClientError(f"Invalid response: {result}. `hour_income` field not found")

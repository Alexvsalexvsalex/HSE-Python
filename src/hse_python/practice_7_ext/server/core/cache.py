from typing import Dict, Optional


class WorkingDaysCache:
    def __init__(self):
        self.working_days: Dict[int, Dict[int, int]] = {}

    def get(self, year: int, month: int) -> Optional[int]:
        return self.working_days.get(year, {}).get(month, None)

    def update(self, year: int, month: int, working_days: int):
        year_cache = self.working_days.get(year, {})
        year_cache[month] = working_days
        self.working_days[year] = year_cache

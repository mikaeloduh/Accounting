from calendar import monthrange
from datetime import datetime


def day_of_month(v):
    return monthrange(v.year_month.year, v.year_month.month)[1]


class Accounting:

    def __init__(self, budget_repo):
        self.repo = budget_repo

    def query_budget(self, start, end):
        str_start = start.strftime('%Y%m')
        str_end = end.strftime('%Y%m')

        # 相差幾天
        total_budget = 0
        for k, v in self.repo.get_all().items():
            if k == str_start and (start.year == end.year) and (start.month == end.month):
                total_budget = v.amount * (end.day - start.day + 1) // day_of_month(v)
                break
            elif k == str_start:
                total_budget = v.amount * (day_of_month(v) - start.day + 1) // day_of_month(v)
            elif str_start < k < str_end:
                total_budget = total_budget + v.amount
            elif k == str_end:
                total_budget = total_budget + (v.amount * end.day // day_of_month(v))
                break

        return total_budget

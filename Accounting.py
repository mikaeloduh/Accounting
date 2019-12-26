

class Accounting:

    def __init__(self, budget_repo):
        self.repo = budget_repo

    def query_budget(self, start, end):

        if start > end:
            return 0

        str_start = start.strftime('%Y%m')
        str_end = end.strftime('%Y%m')

        total_budget = 0
        for k, v in self.repo.get_all().items():
            if k == str_start and (start.year == end.year) and (start.month == end.month):
                total_budget = self.get_daily_budget(v) * (end.day - start.day + 1)
                break
            elif k == str_start:
                total_budget = total_budget + self.get_daily_budget(v) * (v.days_in_month() - start.day + 1)
            elif str_start < k < str_end:
                total_budget = total_budget + v.amount
            elif k == str_end:
                total_budget = total_budget + self.get_daily_budget(v) * end.day

        return total_budget

    @staticmethod
    def get_daily_budget(v):
        return v.amount // v.days_in_month()

from calendar import monthrange


class BudgetModel:

    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount

    def days_in_month(self):
        return monthrange(self.year_month.year, self.year_month.month)[1]

    def get_daily_budget(self):
        return self.amount // self.days_in_month()

from calendar import monthrange


class BudgetModel:

    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount

    def day_of_month(self):
        return monthrange(self.year_month.year, self.year_month.month)[1]

class BudgetManager:
    def __init__(self, amount):
        self.available = 2500.00
        self.budgets = {}
        self.expenditure = {}

    def add_budget(self, name, amount):
        global available
        if name in self.budgets:
            raise ValueError("Budget exists")
        if amount > self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = amount
        self.available -= amount
        self.expenditure[name] = 0
        return self.available

    def spend(self, name, amount):
        if name not in self.expenditure:
            raise ValueError("No such budget")
        self.expenditure[name] += amount
        budgeted = self.budgets[name]
        spent = self.expenditure[name]
        return budgeted - spent

    def print_summary(self):
        print("   Budget       Budgeted      Spent     Remaining")
        print("------------ -------------- ----------- ------------")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenditure[name]
            remaining = budgeted - spent
            print(f'{name:15s} {budgeted:10.2f}{spent:10.2f}'
                f'{remaining:10.2f}')
            total_budgeted += budgeted
            total_spent += spent
            total_remaining += remaining
        print("------------ -------------- ----------- ------------")
        print(f'{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f}'
                f'{total_remaining - total_spent:10.2f}')

outgoings = BudgetManager(2000)
outgoings.available
outgoings.budgets
outgoings.expenditure
outgoings.add_budget("Rent", 700)
outgoings.add_budget("Groceries", 400)
outgoings.add_budget("Bills", 300)
outgoings.add_budget("Entertainment", 100)
outgoings.budgets
outgoings.spend("Groceries", 35)
outgoings.print_summary()

# expense_tracker.py

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, amount, description, category):
        if date not in self.expenses:
            self.expenses[date] = []
        self.expenses[date].append({"amount": amount, "description": description, "category": category})

    def get_expenses(self, date=None):
        if date:
            return self.expenses.get(date, [])
        else:
            return self.expenses

    def get_monthly_summary(self, year, month):
        monthly_expenses = [expense for date, expenses in self.expenses.items() for expense in expenses if date.startswith(f"{year}-{month}-")]
        total_amount = sum(expense["amount"] for expense in monthly_expenses)
        return {"total_amount": total_amount, "expenses": monthly_expenses}

    def get_category_wise_expenditure(self, category):
        category_expenses = [expense for expenses in self.expenses.values() for expense in expenses if expense["category"] == category]
        total_amount = sum(expense["amount"] for expense in category_expenses)
        return {"total_amount": total_amount, "expenses": category_expenses}

    def display_expenses(self):
        for date, expenses in self.expenses.items():
            print(f"Date: {date}")
            for expense in expenses:
                print(f"  Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Get Monthly Summary")
        print("4. Get Category-wise Expenditure")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            category = input("Enter category: ")
            tracker.add_expense(date, amount, description, category)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD) or leave blank for all expenses: ")
            if date:
                expenses = tracker.get_expenses(date)
                if expenses:
                    for expense in expenses:
                        print(f"  Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")
                else:
                    print("No expenses found for the given date.")
            else:
                tracker.display_expenses()
        elif choice == "3":
            year = input("Enter year: ")
            month = input("Enter month: ")
            summary = tracker.get_monthly_summary(year, month)
            print(f"Monthly summary for {year}-{month}:")
            print(f"  Total amount: {summary['total_amount']}")
            for expense in summary["expenses"]:
                print(f"  Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")
        elif choice == "4":
            category = input("Enter category: ")
            expenditure = tracker.get_category_wise_expenditure(category)
            print(f"Category-wise expenditure for {category}:")
            print(f"  Total amount: {expenditure['total_amount']}")
            for expense in expenditure["expenses"]:
                print(f"  Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
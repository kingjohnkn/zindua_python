import csv
from datetime import datetime


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = set()

    def add_expense(self, category, amount):
        expense = {
            "category": category,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d"),
        }
        self.expenses.append(expense)
        self.categories.add(category)
        print(f"Expense of {amount} added in the category {category}.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for expense in self.expenses:
            print(
                f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}"
            )

    def view_category_spending(self):
        if not self.expenses:
            print("No expenses found.")
            return

        category_totals = {}
        for expense in self.expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        print("Category Spending Report:")
        for category, total in category_totals.items():
            print(f"{category}: {total}")

    def view_overall_spending(self):
        if not self.expenses:
            print("No expenses found.")
            return

        total_spending = sum(expense["amount"] for expense in self.expenses)
        print(f"Total Spending: {total_spending}")

    def view_total_savings(self, income):
        if not self.expenses:
            print("No expenses found.")
            return

        total_spending = sum(expense["amount"] for expense in self.expenses)
        total_savings = income - total_spending
        print(f"Total Savings: {total_savings}")

    def generate_monthly_report(self, month, year):
        if not self.expenses:
            print("No expenses found.")
            return

        monthly_expenses = [
            expense
            for expense in self.expenses
            if datetime.strptime(expense["date"], "%Y-%m-%d").month == month
            and datetime.strptime(expense["date"], "%Y-%m-%d").year == year
        ]

        if not monthly_expenses:
            print("No expenses found for the specified month and year.")
            return

        monthly_total = sum(expense["amount"] for expense in monthly_expenses)
        print(f"Monthly Report for {month}/{year}:")
        print(f"Total Spending: {monthly_total}")
        self.view_category_spending()

    def generate_annual_report(self, year):
        if not self.expenses:
            print("No expenses found.")
            return

        annual_expenses = [
            expense
            for expense in self.expenses
            if datetime.strptime(expense["date"], "%Y-%m-%d").year == year
        ]

        if not annual_expenses:
            print("No expenses found for the specified year.")
            return

        annual_total = sum(expense["amount"] for expense in annual_expenses)
        print(f"Annual Report for {year}:")
        print(f"Total Spending: {annual_total}")
        self.view_category_spending()

    def suggest_budget(self):
        if not self.expenses:
            print("No expenses found.")
            return

        category_budgets = {}
        for category in self.categories:
            total_spending = sum(
                expense["amount"]
                for expense in self.expenses
                if expense["category"] == category
            )
            average_spending = total_spending / len(self.expenses)
            category_budgets[category] = average_spending

        print("Suggested Budgets:")
        for category, budget in category_budgets.items():
            print(f"{category}: {budget}")

    def save_expenses_to_file(self, filename):
        if not self.expenses:
            print("No expenses found.")
            return

        try:
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Category", "Amount", "Date"])
                for expense in self.expenses:
                    writer.writerow(
                        [expense["category"], expense["amount"], expense["date"]]
                    )
            print(f"Expenses saved to {filename} successfully.")
        except IOError:
            print("Error occurred while saving expenses to file.")

    def load_expenses_from_file(self, filename):
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    category = row[0]
                    amount = float(row[1])
                    date = row[2]
                    expense = {"category": category, "amount": amount, "date": date}
                    self.expenses.append(expense)
                    self.categories.add(category)
            print(f"Expenses loaded from {filename} successfully.")
        except IOError:
            print("Error occurred while loading expenses from file.")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Category Spending")
        print("4. View Overall Spending")
        print("5. View Total Savings")
        print("6. Generate Monthly Report")
        print("7. Generate Annual Report")
        print("8. Suggest Budget")
        print("9. Save Expenses to File")
        print("10. Load Expenses from File")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            category = input("Enter the category of the expense: ")
            amount = float(input("Enter the amount spent: "))
            tracker.add_expense(category, amount)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_category_spending()

        elif choice == "4":
            tracker.view_overall_spending()

        elif choice == "5":
            income = float(input("Enter your income: "))
            tracker.view_total_savings(income)

        elif choice == "6":
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            tracker.generate_monthly_report(month, year)

        elif choice == "7":
            year = int(input("Enter the year: "))
            tracker.generate_annual_report(year)

        elif choice == "8":
            tracker.suggest_budget()

        elif choice == "9":
            filename = input("Enter the filename to save expenses: ")
            tracker.save_expenses_to_file(filename)

        elif choice == "10":
            filename = input("Enter the filename to load expenses from: ")
            tracker.load_expenses_from_file(filename)

        elif choice == "11":
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

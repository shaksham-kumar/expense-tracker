import json
import os

FILENAME = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file if it exists, otherwise return an empty list."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    """Save the current list of expenses to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g. food, travel, rent): ")
    note = input("Enter a short note: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense['date']} | {expense['category']} | ₹{expense['amount']} | {expense['note']}")
    print()


def view_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total spending: ₹{total}\n")


def view_by_category(expenses):
    category = input("Enter category to filter by: ")
    found = False
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(f"{expense['date']} | ₹{expense['amount']} | {expense['note']}")
            total += expense["amount"]
            found = True

    if not found:
        print("No expenses found in that category.\n")
    else:
        print(f"Total for {category}: ₹{total}\n")


def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return

    try:
        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(f"Deleted: {removed['category']} - ₹{removed['amount']}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    expenses = load_expenses()

    while True:
        print("---- Expense Tracker ----")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View total spending")
        print("4. View expenses by category")
        print("5. Delete an expense")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            view_by_category(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
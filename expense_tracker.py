import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category (Food, Travel, etc.): ")
    amount = float(input("Amount (₹): "))
    description = input("Description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✔ Expense added successfully.\n")


def view_expenses():
    print("\n--- Expense Records ---")

    if not os.path.exists(FILE_NAME):
        print("No expense records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        total = 0
        for row in reader:
            print(f"Date: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]} | Note: {row[3]}")
            total += float(row[2])
        print(f"\nTotal Expenses: ₹{total:.2f}\n")


def search_by_category():
    print("\n--- Search Expenses by Category ---")
    category = input("Enter category to search: ").lower()

    if not os.path.exists(FILE_NAME):
        print("No expense records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row[1].lower() == category:
                print(f"Date: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]} | Note: {row[3]}")
                found = True

        if not found:
            print("No expenses found for this category.\n")


def main_menu():
    while True:
        print("==== EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice. Try again!\n")


if __name__ == "__main__":
    main_menu()

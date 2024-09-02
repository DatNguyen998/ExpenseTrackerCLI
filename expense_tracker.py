import csv
from datetime import datetime

expenses = []

def add_expense(description, amount, category=None):
    expense = {
        'id': len(expenses) + 1,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'description': description,
        'amount': float(amount),
        'category': category
    }
    expenses.append(expense)

def update_expense(expense_id, new_description=None, new_amount=None, new_category=None):
    for expense in expenses:
        if expense['id'] == expense_id:
            if new_description:
                expense['description'] = new_description
            if new_amount:
                expense['amount'] = float(new_amount)
            if new_category:
                expense['category'] = new_category
            return True
    return False

def delete_expense(expense_id):
    global expenses
    expenses = [expense for expense in expenses if expense['id'] != expense_id]

def view_expenses():
    for expense in expenses:
        print(expense)

def summary_all_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")

def summary_expenses_by_month(month):
    month_expenses = [expense for expense in expenses if expense['date'].startswith(f'2024-{month:02d}')]
    total = sum(expense['amount'] for expense in month_expenses)
    print(f"Total Expenses for month {month}: ${total:.2f}")

def export_to_csv(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Date', 'Description', 'Amount', 'Category'])
        for expense in expenses:
            writer.writerow([expense['id'], expense['date'], expense['description'], expense['amount'], expense['category']])

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. View All Expenses")
        print("5. View Summary of All Expenses")
        print("6. View Summary by Month")
        print("7. Export to CSV")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            category = input("Enter category (optional): ")
            add_expense(description, amount, category)
        elif choice == '2':
            expense_id = int(input("Enter expense ID to update: "))
            new_description = input("Enter new description (leave blank to keep current): ")
            new_amount = input("Enter new amount (leave blank to keep current): ")
            new_category = input("Enter new category (leave blank to keep current): ")
            update_expense(expense_id, new_description, new_amount, new_category)
        elif choice == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
        elif choice == '4':
            view_expenses()
        elif choice == '5':
            summary_all_expenses()
        elif choice == '6':
            month = int(input("Enter month (1-12): "))
            summary_expenses_by_month(month)
        elif choice == '7':
            filename = input("Enter filename to export to (e.g., expenses.csv): ")
            export_to_csv(filename)
        elif choice == '8':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

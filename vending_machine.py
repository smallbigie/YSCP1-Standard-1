# vending_machine.py

# Display menu
def display_menu():
    print("Welcome to the Python Vending Machine!")
    print("1. Soda - $1.25")
    print("2. Chips - $1.00")
    print("3. Candy - $0.75")
    print("Enter 'q' to quit.")

# Calculate change (intentional logic error: incorrect subtraction)
def calculate_change(payment, cost):
    return payment - cost - 0.10  # Intentional error

def vending_machine():
    items = {"1": 1.25, "2": 1.00, "3": 0.75}
    while True:
        display_menu()
        choice = input("Select an item (1-3) or 'q' to quit: ")

        if choice == 'q':
            print("Thank you for using the vending machine!")
            break

        if choice not in items:
            print("Invalid selection. Please choose again.")
            continue

        try:
            payment = float(input(f"Enter payment for item (${items[choice]}): "))
            if payment < items[choice]:
                print("Insufficient payment. Transaction canceled.")
                continue
            change = calculate_change(payment, items[choice])
            print(f"Your change is ${change:.2f}. Enjoy your snack!")
        except ValueError:  # Handle non-numeric input
            print("Invalid input. Please enter a numeric value.")

# Intentional syntax error: missing parentheses
if __name__ == "__main__":
    vending_machine()

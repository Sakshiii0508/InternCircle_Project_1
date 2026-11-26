
# Project 1: Interactive Calculator & Unit Converter
# InternCircle - Python Programming


# Conversion factors
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}


# Function to safely read a number
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Arithmetic functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Unit conversion functions
def km_to_miles(km):
    return km * CONVERSION_FACTORS["km_to_miles"]


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def kg_to_pounds(kg):
    return kg * CONVERSION_FACTORS["kg_to_pounds"]


# Function to display unit conversion menu
def unit_converter():
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            km = read_number("Enter kilometers: ")
            print("Miles:", km_to_miles(km))

        elif choice == "2":
            celsius = read_number("Enter temperature in Celsius: ")
            print("Fahrenheit:", celsius_to_fahrenheit(celsius))

        elif choice == "3":
            kg = read_number("Enter weight in kilograms: ")
            print("Pounds:", kg_to_pounds(kg))

        elif choice == "4":
            break

        else:
            print("Invalid choice! Please select from 1 to 4.")


# Main calculator function
def main():
    while True:
        print("\n===== INTERACTIVE CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Unit Conversion")
        print("6. Quit")

        choice = input("Enter your choice: ").strip()

        if choice in ("1", "2", "3", "4"):
            a = read_number("Enter first number: ")
            b = read_number("Enter second number: ")

            if choice == "1":
                print("Addition result:", add(a, b))

            elif choice == "2":
                print("Subtraction result:", subtract(a, b))

            elif choice == "3":
                print("Multiplication result:", multiply(a, b))

            elif choice == "4":
                print("Division result:", divide(a, b))

        elif choice == "5":
            unit_converter()

        elif choice == "6":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Please select from 1 to 6.")


# Start the program
if __name__ == "__main__":
    main()

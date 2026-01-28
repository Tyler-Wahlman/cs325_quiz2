def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Choose an operation (1 or 2): ")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if choice == "1":
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
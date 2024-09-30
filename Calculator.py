import math

def calculator():
    while True:
        print("\nAdvanced Calculator")
        print("1. Basic Arithmetic Operations")
        print("2. Trigonometric Operations")
        print("3. Exponential Operations")
        print("4. Logarithmic Operations")
        print("5. Root Operations")
        print("6. Statistics Operations")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            basic_arithmetic()

        elif choice == '2':
            trigonometric_operations()

        elif choice == '3':
            exponential_operations()

        elif choice == '4':
            logarithmic_operations()

        elif choice == '5':
            root_operations()

        elif choice == '6':
            statistics_operations()

        else:
            print("Invalid choice")
            continue

        # Ask the user if they want to perform another operation
        another_operation = input("Do you want to perform another operation? (y/n): ").lower()
        if another_operation != 'y':
            print("Thank you! Goodbye!")
            break

def basic_arithmetic():
    print("Basic Arithmetic Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", num1 + num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1 - num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1 * num2)

        elif choice == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", num1 / num2)
            else:
                print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice")

def trigonometric_operations():
    print("Trigonometric Operations")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")

    choice = input("Enter your choice (1/2/3): ")

    if choice in ('1', '2', '3'):
        num = float(input("Enter a number (in degrees): "))

        if choice == '1':
            print("sin(", num, ") =", math.sin(math.radians(num)))

        elif choice == '2':
            print("cos(", num, ") =", math.cos(math.radians(num)))

        elif choice == '3':
            if num != 90 and num != 270:
                print("tan(", num, ") =", math.tan(math.radians(num)))
            else:
                print("Error! Tangent is not defined for 90 and 270 degrees.")
    else:
        print("Invalid choice")

def exponential_operations():
    print("Exponential Operations")
    print("1. Exponentiation")
    print("2. Power")

    choice = input("Enter your choice (1/2): ")

    if choice in ('1', '2'):
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter exponent: "))

        if choice == '1':
            print(num1, "^", num2, "=", num1 ** num2)

        elif choice == '2':
            print(num1, "to the power of", num2, "=", num1 ** num2)
    else:
        print("Invalid choice")

def logarithmic_operations():
    print("Logarithmic Operations")
    print("1. Natural Logarithm")
    print("2. Base-10 Logarithm")

    choice = input("Enter your choice (1/2): ")

    if choice in ('1', '2'):
        num = float(input("Enter a number: "))

        if num > 0:
            if choice == '1':
                print("ln(", num, ") =", math.log(num))

            elif choice == '2':
                print("log10(", num, ") =", math.log10(num))
        else:
            print("Error! Logarithm is not defined for non-positive numbers.")
    else:
        print("Invalid choice")

def root_operations():
    print("Root Operations")
    print("1. Square Root")
    print("2. Cube Root")

    choice = input("Enter your choice (1/2): ")

    if choice in ('1', '2'):
        num = float(input("Enter a number: "))

        if choice == '1':
            if num >= 0:
                print("sqrt(", num, ") =", math.sqrt(num))
            else:
                print("Error! Square root is not defined for negative numbers.")

        elif choice == '2':
            print("cbrt(", num, ") =", round(num ** (1/3), 3))
    else:
        print("Invalid choice")

def statistics_operations():
    print("Statistics Operations")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")

    choice = input("Enter your choice (1/2/3): ")

    if choice in ('1', '2', '3'):
        numbers = input("Enter a list of numbers (separated by spaces): ")
        numbers = [float(num) for num in numbers.split()]

        if choice == '1':
            print("Mean:", sum(numbers) / len(numbers))

        elif choice == '2':
            numbers.sort()
            if len(numbers) % 2 == 0:
                median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
            else:
                median = numbers[len(numbers) // 2]
            print("Median:", median)

        elif choice == '3':
            frequency = {}
            for num in numbers:
                frequency[num] = frequency.get(num, 0) + 1
            max_frequency = max(frequency.values())
            modes = [num for num, freq in frequency.items() if freq == max_frequency]
            print("Mode(s):", modes)
    else:
        print("Invalid choice")

calculator()

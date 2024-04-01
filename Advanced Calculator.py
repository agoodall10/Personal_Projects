import math

def basic_calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("That is not a valid number")

    op = input("Enter operator (+, -, *, /, ^): ")

    if op in ['+', '-', '*', '/', '^']:
        while True:
            try:
                num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("That is not a valid number")

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Undefined")
        elif op == "^":
            print("Result:", num1 ** num2)
    else:
        print("Invalid operator")

def scientific_calculator():
    print("Scientific Calculator Options:")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    print("4. Square Root (sqrt)")
    print("5. Exponent (exp)")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        while True:
            try:
                angle = float(input("Enter the angle in degrees: "))
                break
            except ValueError:
                print("That is not a valid number")
        print("Result:", math.sin(math.radians(angle)))
    elif choice == '2':
        while True:
            try:
                angle = float(input("Enter the angle in degrees: "))
                break
            except ValueError:
                print("That is not a valid number")
        print("Result:", math.cos(math.radians(angle)))
    elif choice == '3':
        while True:
            try:
                angle = float(input("Enter the angle in degrees: "))
                break
            except ValueError:
                print("That is not a valid number")
        print("Result:", math.tan(math.radians(angle)))
    elif choice == '4':
        while True:
            try:
                num = float(input("Enter a number: "))
                break
            except ValueError:
                print("That is not a valid number")
        print("Result:", math.sqrt(num))
    elif choice == '5':
        while True:
            try:
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                break
            except ValueError:
                print("That is not a valid number")
        print("Result:", math.pow(base, exponent))
    else:
        print("Invalid choice")

def main():
    print("Select Calculator Type:")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        basic_calculator()
    elif choice == '2':
        scientific_calculator()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

while True:
    print("Welcome to Nhat's Calculator!")

    try:
        a = int(input("Type the first number: "))
        b = int(input("Type the second number: "))
    except ValueError:
        print("We're sorry, that is out of my field.")
        continue

    op = input("Choose t12he operator (+, -, *, /): ")

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("This number is invalid (cannot divide by 0)")
            continue
        else:
            result = a / b
    else:
        print("Invalid operator. Please choose one of +, -, *, /.")
        continue

    print("Result:", result)

    choice = input("Do you want to keep using the calculator (yes/no): ").lower()
    if choice not in ["yes", "y"]:
        print("Goodbye!")
        break

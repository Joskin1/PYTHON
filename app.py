operator = input("Enter an operator (+, -, *, /): ")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if operator == "+":
    result = float(num1) + float(num2)
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = float(num1) - float(num2)
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = float(num1) * float(num2)
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if float(num2) == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = float(num1) / float(num2)
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operator. Please use one of +, -, *, or /.") 
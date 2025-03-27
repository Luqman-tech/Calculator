# input the numbers needed for operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operation (+,-,*,/): ")

# select operator
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:  # avoid division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operator! Enter +, -, *, or /")

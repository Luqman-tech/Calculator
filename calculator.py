import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x, base=10):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(x)

def calculator():
    while True:
        print("\nScientific Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Logarithm")
        print("8. Sine")
        print("9. Cosine")
        print("10. Tangent")
        print("11. Factorial")
        print("12. Exit")
        
        choice = input("Select an operation (1-12): ")
        
        if choice == '12':
            print("Exiting calculator. Goodbye!")
            break
        #select simple operations
        try:
            if choice in ['1', '2', '3', '4', '5']:
                #input the numbers needed for operation
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                operations = {
                    '1': add(num1, num2),
                    '2': subtract(num1, num2),
                    '3': multiply(num1, num2),
                    '4': divide(num1, num2),
                    '5': power(num1, num2)
                }
                print(f"Result: {operations[choice]}")

            #select complex operations
            elif choice in ['6', '7', '8', '9', '10', '11']:
                num = float(input("Enter number: "))
                
                operations = {
                    '6': sqrt(num),
                    '7': log(num),
                    '8': sin(num),
                    '9': cos(num),
                    '10': tan(num),
                    '11': factorial(int(num))
                }
                print(f"Result: {operations[choice]}")
            
            else:
                print("Invalid choice. Please select a valid option.")
        
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")
        

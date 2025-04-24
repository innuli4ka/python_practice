import sys

def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
    return result

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result

def divide(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        if n == 0:
            raise ValueError("Error: Cannot divide by zero.")
        result /= n
    return result

def calculator():
    if len(sys.argv) < 4:
        print("Enter the calculation that you want to perform in the format: number operation numnber")
        return

    operation = sys.argv[2]
    try:
        numbers = [float(arg) for i, arg in enumerate(sys.argv[1:]) if i != 1]
    except ValueError:
        print("Error: All numbers must be valid numeric values.")
        return

    try:
        if operation == "+":
            result = add(numbers)
        elif operation == "-":
            result = subtract(numbers)
        elif operation == "*":
            result = multiply(numbers)
        elif operation == "/":
            result = divide(numbers)
        else:
            print("Error: Unsupported operation. Use +, -, *, or /")
            return

        print(f"Result: {result}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    calculator()

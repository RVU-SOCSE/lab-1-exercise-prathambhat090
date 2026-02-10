print("simple calculator program")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

print("\n\ntemperature inter-conversion")
temp = float(input("Enter the temperature: "))  
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
if unit.upper() == 'C':
    converted_temp = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted_temp}°F")
elif unit.upper() == 'F':
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")

print("\n\nto find the largest and the smallest among three numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))    
num3 = float(input("Enter the third number: "))
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
print("Largest number:", largest)
print("Smallest number:", smallest)



print("simple calculator program")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number to find its factorial: "))
if number < 0:
    print("Error: Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is: {factorial(number)}")

print("\n\nword count in a sentence")
sentence = input("Enter a sentence to count the number of words: ")
words = sentence.split()
word_count = len(words)
print(f"The number of words in the sentence is: {word_count}")

print("\n\nprint fibonacci series")
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
terms = int(input("\nEnter the number of terms for Fibonacci series: "))
if terms <= 0:
    print("Error: Number of terms must be a positive integer.")
else:
    print(f"Fibonacci series up to {terms} terms: {fibonacci(terms)}")

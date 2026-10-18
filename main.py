def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 0


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def reverse_text(text):
    return text[::-1]


if __name__ == "__main__":
    print(greet("World"))
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("6 * 7 =", multiply(6, 7))
    print("20 / 4 =", divide(20, 4))
    print("5 / 0 =", divide(5, 0))
    print("5! =", factorial(5))
    print("Reverse of 'python':", reverse_text("python"))

    for i in range(1, 6):
        print(i, "is even" if is_even(i) else "is odd")

    fruits = ["apple", "banana", "mango"]
    for fruit in fruits:
        print("I like", fruit)

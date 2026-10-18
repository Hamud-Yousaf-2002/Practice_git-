def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0




def is_odd(n):
    return n % 2 == 0





if __name__ == "__main__":
    print(greet("World"))
    print("2 + 3 =", add(2, 3))

    for i in range(1, 6):
        print(i, "is even" if is_even(i) else "is odd")

from multiprocessing import Pool

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def square(n):
    return n * n

def cube(n):
    return n * n * n

if __name__ == "__main__":
    numbers = list(range(1, 11))
    with Pool() as pool:
        fib = pool.map(fibonacci, numbers)
        fact = pool.map(factorial, numbers)
        sq = pool.map(square, numbers)
        cub = pool.map(cube, numbers)

    print(f"Fibonacci: {fib}")
    print(f"Factorial: {fact}")
    print(f"Squares: {sq}")
    print(f"Cubics: {cub}")
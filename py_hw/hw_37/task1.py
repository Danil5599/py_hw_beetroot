import asyncio

async def async_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

async def async_factorial(n):
    if n == 0:
        return 1
    else:
        return n * await async_factorial(n-1)

async def async_square(n):
    return n * n

async def async_cube(n):
    return n * n * n

async def main():
    numbers = list(range(1, 11))
    fib = await asyncio.gather(*(async_fibonacci(n) for n in numbers))
    fact = await asyncio.gather(*(async_factorial(n) for n in numbers))
    sq = await asyncio.gather(*(async_square(n) for n in numbers))
    cub = await asyncio.gather(*(async_cube(n) for n in numbers))

    print(f"Fibonacci: {fib}")
    print(f"Factorial: {fact}")
    print(f"Squares: {sq}")
    print(f"Cubics: {cub}")

asyncio.run(main())
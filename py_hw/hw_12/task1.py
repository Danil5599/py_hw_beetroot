def logger(func):
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        signature = ", ".join(args_repr)
        print(f"{func.__name__} called with {signature}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(1, 2, 3, 4)


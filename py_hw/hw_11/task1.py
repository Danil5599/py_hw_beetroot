def count_variables(func):
    return len(func.__code__.co_varnames)

def test_function():
    x = 10
    y = 20
    name = "John"
    return x + y

print(count_variables(test_function))
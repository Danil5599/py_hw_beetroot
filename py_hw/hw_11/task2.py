def outer_function():
    def inner_function():
        return "Hello from the inner function!"
    return inner_function

func = outer_function()
print(func()) 
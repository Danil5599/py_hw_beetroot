def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(name):
            if not isinstance(name, type_):
                print(f"Error: Argument should be of type {type_}")
                return False
            if len(name) > max_length:
                print(f"Error: Argument length should be less than {max_length}")
                return False
            for item in contains:
                if item not in name:
                    print(f"Error: Argument should contain {item}")
                    return False
            return func(name)
        return wrapper
    return decorator

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('05years'))
print(create_slogan('S@SH05'))
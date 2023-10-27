# IndexError
def oops():
    raise IndexError("Вызвано исключение IndexError!")

def call_oops():
    try:
        oops()
    except IndexError as e:
        print(f"Перехвачено исключение: {e}")

call_oops()


# KeyError
def oops():
    raise KeyError("Вызвано исключение KeyError!")

def call_oops():
    try:
        oops()
    except KeyError as e:
        print(f"Перехвачено исключение: {e}")

call_oops()
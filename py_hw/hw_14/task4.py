class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open("logs.txt", "a") as log_file:
            log_file.write(msg + "\n")

try:
    raise CustomException("This is a custom exception!")
except CustomException as e:
    print(e)

# Проверка содержимого файла logs.txt
with open("logs.txt", "r") as log_file:
    print("Logs:")
    print(log_file.read())

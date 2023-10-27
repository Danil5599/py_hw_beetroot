class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file_obj = None
        self.counter = 0

    def __enter__(self):
        self.file_obj = open(self.filename, self.mode)
        print(f"File {self.filename} opened in {self.mode} mode.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file_obj:
            self.file_obj.close()
            print(f"File {self.filename} closed.")
        with open("log.txt", "a") as log:
            log_message = f"{self.filename} was opened {self.counter} times\n"
            log.write(log_message)
            print(log_message)  # Вывод в консоль

    def read(self, *args, **kwargs):
        self.counter += 1
        content = self.file_obj.read(*args, **kwargs)
        print(f"Read from file {self.filename}: {content}")
        return content

    def write(self, *args, **kwargs):
        self.counter += 1
        result = self.file_obj.write(*args, **kwargs)
        print(f"Written to file {self.filename}: {args[0]}")
        return result

with FileContextManager("sample.txt", "w") as f:
    f.write("Hello, World!")
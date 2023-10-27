import os
import unittest


class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.counter = 0

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        self.counter += 1
        with open("log.txt", "a") as log:
            log_message = f"{self.filename} was opened {self.counter} times\n"
            log.write(log_message)
            print(log_message)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing {self.filename}")
        self.file.close()


class FileContextManagerTest(unittest.TestCase):

    def setUp(self):
        with open("temp.txt", "w") as f:
            f.write("Hello World!")

        with open("log.txt", "w") as log:
            log.write("")

    def tearDown(self):
        if os.path.exists("temp.txt"):
            os.remove("temp.txt")
        if os.path.exists("log.txt"):
            os.remove("log.txt")
        if os.path.exists("newfile.txt"):
            os.remove("newfile.txt")

    def test_multiple_writes(self):
        print("\nExecuting test_multiple_writes")
        with FileContextManager("temp.txt", "w") as f:
            f.write("Hello")
            f.write(" World!")

    def test_read_and_write(self):
        print("\nExecuting test_read_and_write")
        with FileContextManager("temp.txt", "w+") as f:
            f.write("Hello World!")
            f.seek(0)
            content = f.read()
            self.assertEqual(content, "Hello World!")

    def test_non_existent_file(self):
        print("\nExecuting test_non_existent_file")
        with self.assertRaises(FileNotFoundError):
            with FileContextManager("nonexistent.txt", "r") as f:
                pass

    def test_create_new_file(self):
        print("\nExecuting test_create_new_file")
        if os.path.exists("newfile.txt"):
            os.remove("newfile.txt")

        with FileContextManager("newfile.txt", "w") as f:
            f.write("New File Content")

        self.assertTrue(os.path.exists("newfile.txt"))


if __name__ == '__main__':
    unittest.main()
import re

class User:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @staticmethod
    def validate(email):
        pattern = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(pattern, email):
            raise ValueError("Invalid Email!")

try:
    user1 = User("test@example.com")
    print(f"User1's email: {user1.email}")
    user2 = User("test.example.com")  # This will raise an error
except ValueError as e:
    print(e)
import random
import string

# Function to generate password
def generate_password(length):
    # Characters to use: letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input! Please enter a number.")

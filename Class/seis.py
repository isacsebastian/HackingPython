import random

print("Random Password Generator 🤖")


letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/|"

all_characters = letters + numbers + special_characters

length = int(input("Enter the length of the password: "))

password = ""
for _ in range(length):
    password += random.choice(all_characters)

print(f"Generated password: {password}")

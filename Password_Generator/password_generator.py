import random
import string

print("----- Password Generator -----")

length = int(input("Enter password length: "))

print("\nChoose password complexity:")
print("1. Only Letters")
print("2. Letters and Numbers")
print("3. Letters, Numbers and Symbols")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    characters = string.ascii_letters
elif choice == "2":
    characters = string.ascii_letters + string.digits
elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice!")
    exit()

password = ""
for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)

import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length (minimum 8): "))

    if length < 8:
        print("Password length must be at least 8")

    else:
        while True:
            print("\nChoose character types:")
            print("1. Uppercase letters")
            print("2. Lowercase letters")
            print("3. Numbers")
            print("4. Symbols")

            choices = input("Enter choices (example: 123): ")

            # Remove duplicate choices
            choices = set(choices)

            if len(choices) < 2:
                print("Please select at least 2 character types.")
                print("Example: 12 or 123 or 1234")
                continue

            characters = ""

            if "1" in choices:
                characters += string.ascii_uppercase

            if "2" in choices:
                characters += string.ascii_lowercase

            if "3" in choices:
                characters += string.digits

            if "4" in choices:
                characters += string.punctuation

            if not characters:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                continue

            password = ''.join(
                random.choice(characters)
                for _ in range(length)
            )

            print("\nGenerated Password:", password)
            break

except ValueError:
    print("Please enter a valid number.")
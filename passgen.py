import random
import string

# Define character sets
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Get user preferences
def get_user_preferences():
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return length, include_uppercase, include_numbers, include_symbols

# Build the character pool
def build_character_pool(include_uppercase, include_numbers, include_symbols):
    pool = lowercase_letters  # Always include lowercase letters
    if include_uppercase:
        pool += uppercase_letters
    if include_numbers:
        pool += digits
    if include_symbols:
        pool += symbols
    return pool

# Generate password
def generate_password(length, pool):
    return ''.join(random.choice(pool) for _ in range(length))

# Main function
def main():
    print("Welcome to the Password Generator!")
    length, include_uppercase, include_numbers, include_symbols = get_user_preferences()
    
    if length < 1:
        print("Password length must be at least 1. Please try again.")
        return

    pool = build_character_pool(include_uppercase, include_numbers, include_symbols)
    
    if not pool:
        print("You must select at least one character type. Please try again.")
        return

    password = generate_password(length, pool)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()

import string
def is_palidrome(text):
    normal_text = ''.join(char.lower() for char in text if char.isalnum())
    return normal_text == normal_text[::-1]
def main():
    print("Palidrome Checker")
    user = input("Enter a word:")
    if is_palidrome(user):
        print("It is a palidrome")
    else:
        print("It's not a palidrome")
if __name__ == "__main__":
    main()

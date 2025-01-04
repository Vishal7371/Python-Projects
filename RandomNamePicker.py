import random
def random_name_picker():
    print("Welcome to Random Name Picker")
    name_input = input("Enter your name seperated by commas :").strip()
    names = [name.strip() for name in name_input.split(",")]
    if not names or all(name == "" for name in names):
        print("No valid names were entered. Please try again.")
        return
    chosen_name=random.choice(names)
    print(f"The randomly name picked for you is : {chosen_name}")
if __name__=="__main__":
    random_name_picker()




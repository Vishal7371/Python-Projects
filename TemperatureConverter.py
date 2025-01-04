def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 
def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
def show_menu():
    print("Welcome to Temperature Conveter ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
def main():
    while True:
        show_menu()
        choice=input("Enter ur chocie (1-7): ").strip()
        try:
            if choice == "1":
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"Result: {celsius_to_fahrenheit(celsius):.2f} °F")
            elif choice == "2":
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f} °C")
            elif choice == "3":
                celsius = float(input("Enter temperature in Celsius: "))
                print(f"Result: {celsius_to_kelvin(celsius):.2f} K")
            elif choice == "4":
                kelvin = float(input("Enter temperature in Kelvin: "))
                print(f"Result: {kelvin_to_celsius(kelvin):.2f} °C")
            elif choice == "5":
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print(f"Result: {fahrenheit_to_kelvin(fahrenheit):.2f} K")
            elif choice == "6":
                kelvin = float(input("Enter temperature in Kelvin: "))
                print(f"Result: {kelvin_to_fahrenheit(kelvin):.2f} °F")
            elif choice == "7":
                print("GoodBye👋")
            else:
                print("Invalid choice!!!")
        except ValueError:
            print("Invalid Input! Please enter a valid number")
if __name__=="__main__":
    main()
    
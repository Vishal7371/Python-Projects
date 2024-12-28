conversion_rates ={
    "USD_TO_INR":82.75,
    "INR_TO_USD":0.012,
    "EUR_TO_USD": 1.10,
    "USD_TO_EUR": 0.91,
    "GBP_TO_USD": 1.25,
    "USD_TO_GBP": 0.80
}
def convert_currency(from_currency,to_currency,amount):
    key = f"{from_currency}_TO_{to_currency}"
    if key in conversion_rates:
        rate=conversion_rates[key]
        converted_amount=amount*rate
        return converted_amount
    else :
        return None
    
# integrate all the thing in the main:
def main():
    print("Welcome to Currency Converter!")
    print("Available Conversion: USD, INR, EUR, GBP")
    from_currency=input("Enter the currency u want to convert from :").upper()
    to_currency=input("Enter the currency u want to convert too :").upper()
    try:
        amount=float(input("Enter the amount in {from_currency}"))
    except ValueError:
        print("Invalid Amount! Please enter valid number")
        return
    result = convert_currency(from_currency, to_currency, amount)
    if result is not None:
        print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
    else:
        print(f"Conversion rate for {from_currency} to {to_currency} is not available!")
    print("Thank you for using Currency-Conveter")
if __name__ == "__main__":
    main()


    

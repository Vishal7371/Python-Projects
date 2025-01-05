import time
def countdown_timer(seconds):
    while seconds > 0:
        minutes,sec=divmod(seconds,60)
        timer = f"{minutes:02}:{sec:02}"
        print(timer,end="\r")
        time.sleep(1)
        seconds -=1
    print("Times Up!!")
def main():
    print("Countdown TImer")
    try:
        total_second = int(input("Enter the countdown timer in seconds:"))
        if total_second <= 0 :
            print("Please enter a positive number")
        else:
            countdown_timer(total_second)
    except ValueError:
        print("Invalid Input")
if __name__ == "__main__":
    main()


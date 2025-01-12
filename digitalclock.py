from tkinter import Label, Tk
import time

# Initialize the main window
app = Tk()
app.title("Digital Clock")
app.geometry("400x150")  # Width x Height
app.resizable(False, False)  # Disable resizing
app.configure(bg="black")  # Background color

# Add a label to display the time
clock_label = Label(
    app, 
    text="", 
    font=("Arial", 48, "bold"), 
    fg="cyan", 
    bg="black"
)
clock_label.pack(pady=30)  # Add some padding

# Function to update the clock dynamically
def update_clock():
    current_time = time.strftime("%H:%M:%S")  # Get time in HH:MM:SS format
    clock_label.config(text=current_time)  # Update the label
    clock_label.after(1000, update_clock)  # Call this function again after 1 second

# Start updating the clock
update_clock()

# Run the Tkinter event loop
app.mainloop()

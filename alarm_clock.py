import tkinter as tk
import time
import winsound

# Function to check and trigger the alarm
def check_alarm():
    alarm_time = alarm_entry.get()
    current_time = time.strftime("%H:%M")

    if alarm_time == current_time:
        status_label.config(text="Time's up!")
        winsound.Beep(1000, 1000)  # Beep for 1 second
    else:
        status_label.config(text="Alarm set for " + alarm_time)
        root.after(1000, check_alarm)  # Check every 1 second

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create and configure GUI elements
status_label = tk.Label(root, text="")
status_label.pack(pady=20)

alarm_entry = tk.Entry(root, font=("Helvetica", 24))
alarm_entry.pack(pady=10)

set_alarm_button = tk.Button(root, text="Set Alarm", command=check_alarm)
set_alarm_button.pack()

# Start the GUI event loop
root.mainloop()

# sudo pacman -S tk

import socket
import tkinter as tk

# Function to get the local IP address
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

# Create the main window
app = tk.Tk()
app.title("Local IP Address")

# Create a label to display the local IP address
ip_label = tk.Label(
    app, text="Your Local IP Address: " + get_local_ip(), font=("Arial", 14)
)
ip_label.pack(pady=20)

# Create an exit button
exit_button = tk.Button(app, text="Exit", command=app.quit, font=("Arial", 12))
exit_button.pack(pady=10)

# Start the main loop
app.mainloop()



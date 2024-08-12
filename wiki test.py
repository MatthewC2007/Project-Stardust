import customtkinter as ctk

# Create the main window
root = ctk.CTk()
root.title("Show/Hide Widget Example")

# Function to show or hide the widget based on radio button selection
def toggle_widget():
    if radio_var.get() == 1:
        widget.pack()
    else:
        widget.pack_forget()

# Create a variable to hold the value of the selected radio button
radio_var = ctk.IntVar(value=0)

# Create radio buttons
radio_button1 = ctk.CTkRadioButton(root, text="Show Widget", variable=radio_var, value=1, command=toggle_widget)
radio_button1.pack()

radio_button2 = ctk.CTkRadioButton(root, text="Hide Widget", variable=radio_var, value=2, command=toggle_widget)
radio_button2.pack()

# Create the widget to show/hide
widget = ctk.CTkButton(root, text="I am a widget")
widget.pack_forget()  # Initially hide the widget

# Run the application
root.mainloop()

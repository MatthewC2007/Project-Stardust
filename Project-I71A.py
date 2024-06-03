import customtkinter as ctk


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green



app = ctk.CTk()  # create CTk window like you do with the Tk window
app.after(0, lambda: app.state('zoomed'))
app.geometry("1000x700")
app.state('normal')


def menu():
    app.loop()

def button_function():
    page1 = ctk.CTkFrame(app)
    page1.pack(fill="both", expand=1)
    
    button = ctk.CTkButton(master=app, text="Menu", command=menu)
    button.place(relx=0.1, rely=0.9, anchor=ctk.E)

def button_function2():
    page2 = ctk.CTkFrame(app)
    page2.pack(fill="both", expand=1)
    
    button = ctk.CTkButton(master=app, text="Menu", command=menu)
    button.place(relx=0.1, rely=0.9, anchor=ctk.E)


# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=app, text="Page 1", command=button_function)
button.place(relx=0.3, rely=0.5, anchor=ctk.E)

button = ctk.CTkButton(master=app, text="Page 2", command=button_function2)
button.place(relx=0.6, rely=0.5, anchor=ctk.W)



app.mainloop()
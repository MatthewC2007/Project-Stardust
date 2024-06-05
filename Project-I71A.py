import customtkinter as ctk


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green



app = ctk.CTk()  # create CTk window like you do with the Tk window
app.after(0, lambda: app.state('zoomed'))
app.geometry("1000x700")
app.state('normal')


def exit():
    quit("Quit") 

def nextpage():
    new_window = ctk.CTkToplevel(app)
    page2 = ctk.CTkFrame(app)
    page2.pack(fill="both", expand=1)

    button = ctk.CTkButton(master=app, text="Volcanoes", command=history)
    button.place(relx=0.2, rely=0.5, anchor=ctk.W)

    button = ctk.CTkButton(master=app, text="Space", command=history)
    button.place(relx=0.45, rely=0.5, anchor=ctk.W)

    button = ctk.CTkButton(master=app, text="History", command=history)
    button.place(relx=0.7, rely=0.5, anchor=ctk.W)

def history():
    new_window = ctk.CTkToplevel(app)
    page2 = ctk.CTkFrame(app)
    page2.pack(fill="both", expand=10)

    button = ctk.CTkButton(master=app, text="button")
    button.place(relx=0.5, rely=0.5, anchor=ctk.W)


# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=app, text="Exit", command=exit)
button.place(relx=0.3, rely=0.7, anchor=ctk.E)

button = ctk.CTkButton(master=app, text="Next", command=nextpage)
button.place(relx=0.6, rely=0.7, anchor=ctk.W)



app.mainloop()
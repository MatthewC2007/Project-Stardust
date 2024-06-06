import customtkinter as ctk
import tkinter as tk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("500x400")

        # Create a frame for the menu page
        self.menu_page = ctk.CTkFrame(self)
        self.menu_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Initialize frames for the other pages but do not place them yet
        self.page_one = ctk.CTkFrame(self)
        self.page_two = ctk.CTkFrame(self)
        self.page_three = ctk.CTkFrame(self)
        self.navigation_page = ctk.CTkFrame(self)

        # Button on the menu page for the navigation page
        self.to_navigation_page_button = ctk.CTkButton(self.menu_page, text="Open Navigation Page", command=self.show_navigation_page)
        self.to_navigation_page_button.pack(pady=10)

        # Buttons on the navigation page to navigate to other pages
        ctk.CTkButton(self.navigation_page, text="To Page One", command=self.show_page_one).pack(pady=10)
        ctk.CTkButton(self.navigation_page, text="To Page Two", command=self.show_page_two).pack(pady=10)
        ctk.CTkButton(self.navigation_page, text="To Page Three", command=self.show_page_three).pack(pady=10)

        # Show the menu page by default
        self.show_menu_page()

    def hide_all_pages(self):
        # Hide all pages
        self.menu_page.place_forget()
        self.page_one.place_forget()
        self.page_two.place_forget()
        self.page_three.place_forget()
        self.navigation_page.place_forget()

    def show_menu_page(self):
        self.hide_all_pages()
        self.menu_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_navigation_page(self):
        self.hide_all_pages()
        self.navigation_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_page_one(self):
        self.hide_all_pages()
        self.page_one.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_page_two(self):
        self.hide_all_pages()
        self.page_two.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_page_three(self):
        self.hide_all_pages()
        self.page_three.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()

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
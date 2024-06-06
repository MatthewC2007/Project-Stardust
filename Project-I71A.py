import customtkinter as ctk
import tkinter as tk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


        self.after(0, lambda: self.state('zoomed'))
        self.geometry("1920x1080")
        self.state('normal')
        
        self.welcome = ctk.CTkFrame(self)
        self.welcome.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Initialize frames for the other pages but do not place them yet
        self.page_one = ctk.CTkFrame(self)
        self.page_two = ctk.CTkFrame(self)
        self.page_three = ctk.CTkFrame(self)
        self.menu_page = ctk.CTkFrame(self)

        # Button on the menu page for the navigation page
        self.to_menu_page_button = ctk.CTkButton(self.welcome, text="Next", command=self.menu)
        self.to_menu_page_button.pack(padx=200,pady=100)

        # Buttons on the navigation page to navigate to other pages
        ctk.CTkButton(self.menu_page, text="P1", command=self.p1).pack(padx=200, pady=50)
        ctk.CTkButton(self.menu_page, text="P2", command=self.p2).pack(padx=200, pady=50)
        ctk.CTkButton(self.menu_page, text="P3", command=self.p3).pack(padx=200, pady=50)

        # Show the menu page by default
        self.show_welcome()
    
    def show_welcome(self):
        self.hide_all_pages()
        self.welcome.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_all_pages(self):
        # Hide all pages
        self.welcome.place_forget()
        self.page_one.place_forget()
        self.page_two.place_forget()
        self.page_three.place_forget()
        self.menu_page.place_forget()
    
    def menu(self):
        self.hide_all_pages()
        self.menu_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def p1(self):
        self.hide_all_pages()
        self.page_one.place(relx=0.1, rely=0.2, anchor=tk.CENTER)
        button = ctk.CTkButton(master=app, text="button")
        button.place(relx=0.5, rely=0.5, anchor=ctk.W)

    def p2(self):
        self.hide_all_pages()
        self.page_two.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def p3(self):
        self.hide_all_pages()
        self.page_three.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()
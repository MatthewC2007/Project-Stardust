import customtkinter as ctk
import tkinter as tk
import wikipedia
from Text import*
  

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


        self.after(0, lambda: self.state('zoomed'))
        self.geometry("1920x1080")
        self.state('normal')
        
        self.welcome = ctk.CTkFrame(self,width=500, height=500)
        self.welcome.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        

        # Initialize frames for the other pages but do not place them yet
        self.page_one = ctk.CTkFrame(self)
        self.page_two = ctk.CTkFrame(self)
        self.page_three = ctk.CTkFrame(self)
        self.menu_page = ctk.CTkFrame(self)
        self.quest_page = ctk.CTkFrame(self)

        #Welcome page

        #Welcome text
        label = ctk.CTkLabel(self.welcome, text="Welcome",
            font=("Harlow Solid Italic",150))
        label.pack(pady=300,padx=500)
        
        #Slogan
        label = ctk.CTkLabel(self.welcome,
            text="Empowering kids through knowledge", font=("Harlow Solid Italic",50))
        label.place(relx=0.5,rely=0.7, anchor=tk.CENTER)
        
        #Next button on Welcome page
        self.to_menu_page_button = ctk.CTkButton(self.welcome, text="Next",
            command=self.menu,height=60, width=120,font=("Helvetica",25))
        self.to_menu_page_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
        
        #Exit button on Welcome page
        self.to_menu_page_button = ctk.CTkButton(self.welcome, text="Exit",    
            command=quit,height=60, width=120,font=("Helvetica",25))
        self.to_menu_page_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)
        

        # Buttons on the navigation page to navigate to other pages
        ctk.CTkButton(self.menu_page, text="P1",
                       command=self.p1).pack(padx=200, pady=50)
        ctk.CTkButton(self.menu_page, text="P2",
                       command=self.p2).pack(padx=200, pady=50)
        ctk.CTkButton(self.menu_page, text="P3",
                       command=self.p3).pack(padx=200, pady=50)
        
        #Page 1
        label = ctk.CTkLabel(self.page_one,
            text=split_string(wikipedia.summary("volcanoes", sentences = 8), 150), font=("Helvetica",25),
              height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_one, text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_one, text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        #Page 2
        label = ctk.CTkLabel(self.page_two,
            text=split_string(wikipedia.summary("Slavery", sentences = 8), 150), font=("Helvetica",25),
              height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_two, text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_two, text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        #page 3
        label = ctk.CTkLabel(self.page_three,
            text=split_string(wikipedia.summary("Japanese Culture", sentences = 8), 150), font=("Helvetica",25),
              height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_three, text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_three, text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        #page 3b
        button = ctk.CTkButton(master=self.quest_page, text="Back",command=self.p3)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
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
        self.quest_page.place_forget()
    
    def menu(self):
        self.hide_all_pages()
        self.menu_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def p1(self):
        self.hide_all_pages()
        self.page_one.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        

    def p2(self):
        self.hide_all_pages()
        self.page_two.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def p3(self):
        self.hide_all_pages()
        self.page_three.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def Questions(self):
        self.hide_all_pages()
        self.quest_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    app = App()
    app.mainloop()
import customtkinter as ctk
import tkinter as tk
import wikipedia
from Text import*
import threading as thread

loaded_websites = {}

class Thread(thread.Thread):
    def __init__(self, website_name: str):
        super().__init__()
        self.website = website_name

    def run(self):
        loaded_websites[self.website] = wikipedia.summary(self.website)

class App(ctk.CTk):
    
    websites = [
        'volcanoes',
        'MLKJ',
        'Japanese Culture',
        'Black hole',
        'Maori wars',
        'Trinity Test',
    ]
    
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


        self.after(0, lambda: self.state('zoomed'))
        self.geometry("1920x1080")
        self.state('normal')
        
        self.welcome = ctk.CTkFrame(self,width=500, height=500)
        self.welcome.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.title("Project-I71A")

        for website_data in enumerate(self.websites):
            self.load_website_async(website_data)

        # gets the pages ready but doesn't place them
        self.page_volc = ctk.CTkFrame(self)
        self.page_MLKJ = ctk.CTkFrame(self)
        self.page_jap = ctk.CTkFrame(self)
        self.menu_page = ctk.CTkFrame(self)
        self.quest_page = ctk.CTkFrame(self)
        self.settings_page = ctk.CTkFrame(self)
        self.page_blackh = ctk.CTkFrame(self)
        self.page_trinity = ctk.CTkFrame(self)
        self.page_maoriw = ctk.CTkFrame(self)

    #Welcome page

        #Welcome text
        label = ctk.CTkLabel(self.welcome, text="Welcome",
            font=("Harlow Solid Italic",150))
        label.pack(pady=300,padx=500)
        
        #Slogan
        label = ctk.CTkLabel(self.welcome,
            text="Empowering kids through knowledge",
              font=("Harlow Solid Italic",50))
        label.place(relx=0.5,rely=0.7, anchor=tk.CENTER)
        
        #Next button on Welcome page
        self.to_menu_page_button = ctk.CTkButton(self.welcome, text="Next",
            command=self.menu,height=60, width=120,font=("Helvetica",25))
        self.to_menu_page_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
        
        #Exit button on Welcome page
        self.to_menu_page_button = ctk.CTkButton(self.welcome, text="Exit",    
            command=quit,height=60, width=120,font=("Helvetica",25))
        self.to_menu_page_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)
        

    # Buttons on the menu page to navigate to other pages
        label = ctk.CTkLabel(self.menu_page, text="Menu",
            font=("Harlow Solid Italic",100))
        label.grid(row = 0, column = 2, columnspan = 1,pady = 60, padx = 60)
        button = ctk.CTkButton(self.menu_page, text="Volcanoes",
            command=self.volc).grid(row = 2, column = 1, pady = 40, padx = 30)
        button = ctk.CTkButton(self.menu_page, text="MLKJ",
            command=self.MLKJ).grid(row = 3, column = 3, pady = 40, padx = 30)
        button = ctk.CTkButton(self.menu_page, text="Japan",
            command=self.Japan).grid(row = 3, column = 1, pady = 40, padx = 30)
        button = ctk.CTkButton(self.menu_page, text="Black holes",
            command=self.Blackhole).grid(row = 2, column = 2, pady = 40, padx = 30)
        button = ctk.CTkButton(self.menu_page, text="Trinity test",
            command=self.Trinity).grid(row = 3, column = 2, pady = 40, padx = 30)
        button = ctk.CTkButton(self.menu_page, text="Maori Wars",
            command=self.MaoriW).grid(row = 2, column = 3, pady = 40, padx = 30)
    
        button = ctk.CTkButton(self.menu_page, text="Back", height=60, width=120,
            command=self.show_welcome, font=("Helvetica",25)).grid(row = 9,
                                             column = 0, pady = 60, padx = 60)
        button = ctk.CTkButton(self.menu_page, text="Quit", height=60, width=120,
            command=self.quit, font=("Helvetica",25)).grid(row = 9,
                                             column = 4, pady = 60, padx = 60)
        button = ctk.CTkButton(self.menu_page,
         text = "Settings", height = 40, width = 120,
         command=self.settings,font=("Helvetica",20)).grid(row = 0, column = 0)
        
        
    #Volcano
        label = ctk.CTkLabel(self.page_volc,
            text=split_string(wikipedia.summary("volcanoes",
                                 sentences = 10), 150), font=("Helvetica",25),
              height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_volc,
                                text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_volc,
                                text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #MLKJ
        label = ctk.CTkLabel(self.page_MLKJ,
            text=split_string(wikipedia.summary("MLKJ",
                                 sentences = 10), 150), font=("Helvetica",25),
              height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_MLKJ,
                                text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_MLKJ,
                                text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Japan culture
        label = ctk.CTkLabel(self.page_jap,
            text=split_string(wikipedia.summary("Japanese Culture",
             sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_jap,
                                text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_jap,
                                text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Black hole
        label = ctk.CTkLabel(self.page_blackh,
            text=split_string(wikipedia.summary("Black hole",
             sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_blackh,
                                text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_blackh,
                                text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Trinity test
        label = ctk.CTkLabel(self.page_trinity,
            text=split_string(wikipedia.summary("Trinity test",
             sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_trinity,
                                text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_trinity,
                                text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Maori Wars
        label = ctk.CTkLabel(self.page_maoriw,
            text=split_string(wikipedia.summary("Maori Wars",
             sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_maoriw,
                                text="Back",command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_maoriw,
                                text="Next", command=self.Questions)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Volc Quiz
        button = ctk.CTkButton(master=self.quest_page,
                                text="Back",command=self.volc)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    #Jap Quiz
        button = ctk.CTkButton(master=self.quest_page,
                                text="Back",command=self.Japan)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    #MLKJ Quiz
        button = ctk.CTkButton(master=self.quest_page,
                                text="Back",command=self.MLKJ)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    #Black Hole Quiz
        button = ctk.CTkButton(master=self.quest_page,
                                text="Back",command=self.Blackhole)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    #Trinity Test Quiz
        button = ctk.CTkButton(master=self.quest_page,
                                text="Back",command=self.Blackhole)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    #Maori Wars Quiz
        button = ctk.CTkButton(master=self.quest_page,
                                text="Back",command=self.Blackhole)
        button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    #Settings Page
        label = ctk.CTkLabel(self.settings_page,
                              text="Settings",font=("Harlow Solid Italic",100))
        label.grid(row = 0, column = 1, columnspan = 1,pady = 60, padx = 60)
        button = ctk.CTkButton(master=self.settings_page,
                                text="Light mode", command=self.light_mode)
        button.grid(row = 5, column = 1, columnspan = 1,pady = 60, padx = 60)
        button = ctk.CTkButton(master=self.settings_page,
                                text="Dark mode", command=self.dark_mode)
        button.grid(row = 5, column = 2, columnspan = 1,pady = 60, padx = 60)
        button = ctk.CTkButton(master=self.settings_page,
                                text="Back", command=self.menu)
        button.grid(row = 5, column = 0, columnspan = 1,pady = 60, padx = 60)
        
    # Show the menu page by default
        self.show_welcome()
    
    def show_welcome(self):
        self.hide_all_pages()
        self.welcome.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_all_pages(self):
        # Hide all pages
        self.welcome.place_forget()
        self.page_volc.place_forget()
        self.page_MLKJ.place_forget()
        self.page_jap.place_forget()
        self.menu_page.place_forget()
        self.quest_page.place_forget()
        self.settings_page.place_forget()
        self.page_blackh.place_forget()
        self.page_maoriw.place_forget()
        self.page_trinity.place_forget()
    
    def menu(self):
        self.hide_all_pages()
        self.menu_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def volc(self):
        self.hide_all_pages()
        self.page_volc.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    def MLKJ(self):
        self.hide_all_pages()
        self.page_MLKJ.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Japan(self):
        self.hide_all_pages()
        self.page_jap.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Blackhole(self):
        self.hide_all_pages()
        self.page_blackh.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Trinity(self):
        self.hide_all_pages()
        self.page_trinity.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def MaoriW(self):
        self.hide_all_pages()
        self.page_maoriw.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Questions(self):
        self.hide_all_pages()
        self.quest_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def settings(self):
        self.hide_all_pages()
        self.settings_page.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

    def dark_mode(self):
        ctk.set_appearance_mode("dark")

    def light_mode(self):
        ctk.set_appearance_mode("light")

    def load_website_async(self, website_data):
        index, website = list(website_data)
        Thread(website).start()

#Sets the mode to dark by default
mode = "dark"

if __name__ == "__main__":
    app = App()
    app.mainloop()
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

        # G ets the pages ready but doesn't place them
        self.page_volc = ctk.CTkFrame(self)
        self.page_volcquiz = ctk.CTkFrame(self)
        self.page_MLKJ = ctk.CTkFrame(self)
        self.page_MLKJquiz = ctk.CTkFrame(self)
        self.page_jap = ctk.CTkFrame(self)
        self.page_japquiz = ctk.CTkFrame(self)
        self.menu_page = ctk.CTkFrame(self)
        self.settings_page = ctk.CTkFrame(self)
        self.page_blackh = ctk.CTkFrame(self)
        self.page_blackhquiz = ctk.CTkFrame(self)
        self.page_trinity = ctk.CTkFrame(self)
        self.page_trinityquiz = ctk.CTkFrame(self)
        self.page_maoriw = ctk.CTkFrame(self)
        self.page_maoriquiz = ctk.CTkFrame(self)

        

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
            command=self.Blackhole).grid(row = 2, column = 2, pady =40, padx=30)
        button = ctk.CTkButton(self.menu_page, text="Trinity test",
            command=self.Trinity).grid(row = 3, column = 2, pady = 40, padx =30)
        button = ctk.CTkButton(self.menu_page, text="Maori Wars",
            command=self.MaoriW).grid(row = 2, column = 3, pady = 40, padx =30)
    
        button = ctk.CTkButton(self.menu_page, text="Back", height=60,width=120,
            command=self.show_welcome, font=("Helvetica",25)).grid(row = 9,
                                             column = 0, pady = 60, padx = 60)
        button = ctk.CTkButton(self.menu_page, text="Quit", height=60, 
            width=120,command=self.quit, font=("Helvetica",25)).grid(row = 9,
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
            text="Back",height=60, width=120,font=("Helvetica",25),
                                                command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_volc,
            text="Next", height=60, width=120,font=("Helvetica",25),
                                                command=self.Volcquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #MLKJ
        label = ctk.CTkLabel(self.page_MLKJ,
            text=split_string(wikipedia.summary("MLKJ",
                                 sentences = 10), 150), font=("Helvetica",25),
              height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_MLKJ,
            text="Back",height=60, width=120,font=("Helvetica",25),
                                                command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_MLKJ,
            text="Next",height=60,width=120,font=("Helvetica",25),
                                                command=self.MLKJquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Japan culture
        label = ctk.CTkLabel(self.page_jap,
            text=split_string(wikipedia.summary("Japanese Culture",
             sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_jap,
            text="Back",height=60, width=120,font=("Helvetica",25),
                                                command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_jap,
            text="Next",height=60, width=120,font=("Helvetica",25),
                                                command=self.Japquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Black hole
        label = ctk.CTkLabel(self.page_blackh,
            text=split_string(wikipedia.summary("Black hole",
             sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_blackh,
            text="Back",height=60, width=120,font=("Helvetica",25),
                                                command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_blackh,
            text="Next",height=60,width=120,font=("Helvetica",25),
                                                command=self.Blackhquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Trinity test
        label = ctk.CTkLabel(self.page_trinity,
            text=split_string(wikipedia.summary("Trinity test",
             sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_trinity,
            text="Back",height=60, width=120,command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_trinity,
            text="Next",height=60, width=120,command=self.Trinityquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

    #Maori Wars
        label = ctk.CTkLabel(self.page_maoriw,
            text=split_string(wikipedia.summary("Maori Wars",
             sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_maoriw,
            text="Back",height=60, width=120,command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_maoriw,
            text="Next",height=60, width=120,command=self.Maoriwquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)        
        

    #Volc Quiz
        def VolcButton():
            if radio_var5.get() == 1:
                button6.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button6.grid_forget()
        label = ctk.CTkLabel(self.page_volcquiz,
                              text="What is a volcano?",
                              font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_volcquiz,
                                text="Back",command=self.volc)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button6 = ctk.CTkButton(master=self.page_volcquiz,
                                text="Next")
        button6.grid_forget()
        radio_var5 = ctk.IntVar(master=self.page_volcquiz,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_volcquiz,
            text="A rupture in the crust", value=1, variable=radio_var5,
                                                        command=VolcButton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_volcquiz,
            text="A spicy hill", value=2,variable=radio_var5,command=VolcButton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_volcquiz,
            text="A mountain", value=3,variable=radio_var5,command=VolcButton)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_volcquiz,
            text="Hot pools", value=4,variable=radio_var5,command=VolcButton)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

    #Jap Quiz
        def JapButton():
            if radio_var4.get() == 1:
                button5.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button5.grid_forget()
        label = ctk.CTkLabel(self.page_japquiz,
                              text="What groups helped shape Japanese Culture?",
                              font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_japquiz,
                                text="Back",command=self.Japan)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button5 = ctk.CTkButton(master=self.page_japquiz,
                                text="Next")
        button5.grid_forget()
        radio_var4 = ctk.IntVar(master=self.page_japquiz,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_japquiz,
            text="The Maori are sigma", value=1, variable=radio_var4,
                                                    command=JapButton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_japquiz,
            text="I like Maccas", value=2,variable=radio_var4,command=JapButton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)

    #MLKJ Quiz
        def MLKJButtob():
            if radio_var3.get() == 1:
                button4.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button4.grid_forget()
        label = ctk.CTkLabel(self.page_MLKJquiz,
                              text="Who is Martin Luther King Junior?"
                              ,font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_MLKJquiz,
                                text="Back",command=self.MLKJ)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button4 = ctk.CTkButton(master=self.page_MLKJquiz,
                                text="Next")
        button4.grid_forget()
        radio_var3 = ctk.IntVar(master=self.page_MLKJquiz,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_MLKJquiz,
            text="The Maori are sigma", value=1, variable=radio_var3,
                                                    command=MLKJButtob)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_MLKJquiz,
            text="I like Maccas", value=2,variable=radio_var3,
                                                    command=MLKJButtob)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        
        
        #Black Hole Quiz
        def BlackHButton():
            if radio_var2.get() == 1:
                button3.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button3.grid_forget()
        label = ctk.CTkLabel(self.page_blackhquiz,
                text="What is a black hole?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_blackhquiz,
                                text="Back",command=self.Blackhole)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button3 = ctk.CTkButton(master=self.page_blackhquiz,
                                text="Next")
        button3.grid_forget()
        radio_var2 = ctk.IntVar(master=self.page_blackhquiz,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_blackhquiz,
            text="The Maori are sigma", value=1, variable=radio_var2,
                                                        command=BlackHButton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_blackhquiz,
            text="I like Maccas", value=2,variable=radio_var2,
                                                        command=BlackHButton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)

        
        #Trinity Test Quiz
        def Trinitybutton():
            if radio_var1.get() == 1:
                button2.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button2.grid_forget()
        label = ctk.CTkLabel(self.page_trinityquiz,
            text="What is the Trimity test?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_trinityquiz,
                                text="Back",command=self.Trinity)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button2 = ctk.CTkButton(master=self.page_trinityquiz,
                                text="Next")
        button2.grid_forget()
        radio_var1 = ctk.IntVar(master=self.page_trinityquiz,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_trinityquiz,
            text="The Maori are sigma", value=2, variable=radio_var1,
                                                    command=Trinitybutton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_trinityquiz,
            text="I like Maccas", value=1,variable=radio_var1,
                                                    command=Trinitybutton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        
        
        #Maori Wars Quiz
        def Maoributton():
            if radio_var.get() == 1:
                button1.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button1.grid_forget()
        label = ctk.CTkLabel(self.page_maoriquiz,
            text="What were the Maori Wars?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_maoriquiz,
                                text="Back",command=self.MaoriW)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button1 = ctk.CTkButton(master=self.page_maoriquiz,
                                text="Next")
        button1.grid_forget()
        radio_var = ctk.IntVar(master=self.page_maoriquiz,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_maoriquiz,
                            text="The Maori are sigma", value=1,
                                variable=radio_var,command=Maoributton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_maoriquiz,
            text="I like Maccas", value=2,variable=radio_var,
                                        command=Maoributton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
          

        
    #Settings Page
        label = ctk.CTkLabel(self.settings_page,
                              text="Settings",font=("Harlow Solid Italic",100))
        label.grid(row = 0, column = 1, columnspan = 1,pady = 60, padx = 60)
        button = ctk.CTkButton(master=self.settings_page,text="Light mode",
            height=60, width=120,font=("Helvetica",25), command=self.light_mode)
        button.grid(row = 5, column = 1, columnspan = 1,pady = 60, padx = 60)
        button = ctk.CTkButton(master=self.settings_page,text="Dark mode",
            height=60, width=120,font=("Helvetica",25),command=self.dark_mode)
        button.grid(row = 5, column = 2, columnspan = 1,pady = 60, padx = 60)
        button = ctk.CTkButton(master=self.settings_page,text="Back",
            height=60, width=120,font=("Helvetica",25), command=self.menu)
        button.grid(row = 5, column = 0, columnspan = 1,pady = 60, padx = 60)
        
    # Show the welcome page by default
        self.show_welcome()
    

    def hide_all_pages(self):
        # Hide all pages
        self.welcome.place_forget()
        self.page_volc.place_forget()
        self.page_MLKJ.place_forget()
        self.page_jap.place_forget()
        self.menu_page.place_forget()
        self.settings_page.place_forget()
        self.page_blackh.place_forget()
        self.page_maoriw.place_forget()
        self.page_trinity.place_forget()
        self.page_trinityquiz.place_forget()
        self.page_maoriquiz.place_forget()
        self.page_blackhquiz.place_forget()
        self.page_japquiz.place_forget()
        self.page_blackhquiz.place_forget()
        self.page_volcquiz.place_forget()
        self.page_MLKJquiz.place_forget()
        
    
    def show_welcome(self):
        self.hide_all_pages()
        self.welcome.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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

    def Volcquiz(self):
        self.hide_all_pages()
        self.page_volcquiz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def MLKJquiz(self):
        self.hide_all_pages()
        self.page_MLKJquiz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Blackhquiz(self):
        self.hide_all_pages()
        self.page_blackhquiz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Japquiz(self):
        self.hide_all_pages()
        self.page_japquiz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Trinityquiz(self):
        self.hide_all_pages()
        self.page_trinityquiz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Maoriwquiz(self):
        self.hide_all_pages()
        self.page_maoriquiz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
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

        #Gets the pages ready but doesn't place them
        self.page_volc = ctk.CTkFrame(self)
        self.page_volcquiz1 = ctk.CTkFrame(self)
        self.page_volcquiz2 = ctk.CTkFrame(self)
        self.page_MLKJ = ctk.CTkFrame(self)
        self.page_MLKJquiz1 = ctk.CTkFrame(self)
        self.page_MLKJquiz2 = ctk.CTkFrame(self)
        self.page_jap = ctk.CTkFrame(self)
        self.page_japquiz1 = ctk.CTkFrame(self)
        self.page_japquiz2 = ctk.CTkFrame(self)
        self.menu_page = ctk.CTkFrame(self)
        self.settings_page = ctk.CTkFrame(self)
        self.page_blackh = ctk.CTkFrame(self)
        self.page_blackhquiz1 = ctk.CTkFrame(self)
        self.page_blackhquiz2 = ctk.CTkFrame(self)
        self.page_trinity = ctk.CTkFrame(self)
        self.page_trinityquiz1 = ctk.CTkFrame(self)
        self.page_trinityquiz2 = ctk.CTkFrame(self)
        self.page_maoriw = ctk.CTkFrame(self)
        self.page_maoriquiz1 = ctk.CTkFrame(self)
        self.page_maoriquiz2 = ctk.CTkFrame(self)
        self.page_credits = ctk.CTkFrame(self)



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
                                                command=self.Volcquiz1)
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
        

    #Volc Quiz Page 1
        def VolcButton():
            if radio_var5.get() == 1:
                button6.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button6.grid_forget()
        label = ctk.CTkLabel(self.page_volcquiz1,
                              text="What is a volcano?",
                              font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_volcquiz1,
                                text="Back",command=self.volc)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button6 = ctk.CTkButton(master=self.page_volcquiz1,
                                text="Next",command=self.Volcquiz2)
        button6.grid_forget()
        radio_var5 = ctk.IntVar(master=self.page_volcquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_volcquiz1,
            text="A rupture in the crust", value=1, variable=radio_var5,
                                                        command=VolcButton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_volcquiz1,
            text="A spicy hill", value=2,variable=radio_var5,command=VolcButton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_volcquiz1,
            text="A mountain", value=3,variable=radio_var5,command=VolcButton)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_volcquiz1,
            text="Hot pools", value=4,variable=radio_var5,command=VolcButton)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

    #Volc Quiz Page 2
        def VolcButtonA():
            if radio_var5a.get() == 1:
                button6a.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button6a.grid_forget()
        label = ctk.CTkLabel(self.page_volcquiz2,
                              text="What is a volcano?",
                              font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_volcquiz2,
                                text="Back",command=self.Volcquiz1)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button6a = ctk.CTkButton(master=self.page_volcquiz2,
                                text="Next",command=self.credits)
        button6a.grid_forget()
        radio_var5a = ctk.IntVar(master=self.page_volcquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_volcquiz2,
            text="A rupture in the crust", value=1, variable=radio_var5a,
                                                        command=VolcButtonA)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_volcquiz2,
            text="A spicy hill", value=2,variable=radio_var5a,command=VolcButtonA)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_volcquiz2,
            text="A mountain", value=3,variable=radio_var5a,command=VolcButtonA)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_volcquiz2,
            text="Hot pools", value=4,variable=radio_var5a,command=VolcButtonA)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)
      
    

    #Japanese Quiz Page 1
        def JapButton():
            if radio_var4.get() == 1:
                button5.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button5.grid_forget()
        label = ctk.CTkLabel(self.page_japquiz1,
                              text="What groups helped shape Japanese Culture?",
                              font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_japquiz1,
                                text="Back",command=self.Japan)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button5 = ctk.CTkButton(master=self.page_japquiz1,
                                text="Next",command=self.Japquiz2)
        button5.grid_forget()
        radio_var4 = ctk.IntVar(master=self.page_japquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_japquiz1,
            text="The Maori are sigma", value=1, variable=radio_var4,
                                                    command=JapButton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_japquiz1,
            text="I like Maccas", value=2,variable=radio_var4,command=JapButton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)

    #Japanese Quiz Page 2
        def JapButtonA():
            if radio_var4a.get() == 1:
                button5a.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button5a.grid_forget()
        label = ctk.CTkLabel(self.page_japquiz2,
                                text="What groups helped shape Japanese Culture?",
                                font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_japquiz2,
                                text="Back",command=self.Japquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button5a = ctk.CTkButton(master=self.page_japquiz2,
                                text="Next",command=self.credits)
        button5a.grid_forget()
        radio_var4a = ctk.IntVar(master=self.page_japquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_japquiz2,
                            text="The Maori are sigma", value=1,
                            variable=radio_var4a,command=JapButtonA)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_japquiz2,
                            text="I like Maccas", 
                            value=2, variable=radio_var4a,command=JapButtonA)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)

        
    #MLKJ Quiz Page 1
        def MLKJButtob():
            if radio_var3.get() == 1:
                button4.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button4.grid_forget()
        label = ctk.CTkLabel(self.page_MLKJquiz1,
                              text="Who is Martin Luther King Junior?"
                              ,font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_MLKJquiz1,
                                text="Back",command=self.MLKJ)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button4 = ctk.CTkButton(master=self.page_MLKJquiz1,
                                text="Next",command=self.MLKJquiz2)
        button4.grid_forget()
        radio_var3 = ctk.IntVar(master=self.page_MLKJquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_MLKJquiz1,
            text="The Maori are sigma", value=1, variable=radio_var3,
                                                    command=MLKJButtob)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_MLKJquiz1,
            text="I like Maccas", value=2,variable=radio_var3,
                                                    command=MLKJButtob)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
    
    #MLKJ Quiz Page 2
        def MLKJButtobA():
            if radio_var3a.get() == 1:
                button4a.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button4a.grid_forget()
        label = ctk.CTkLabel(self.page_MLKJquiz2,
                                text="Who is Martin Luther King Junior?"
                                ,font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_MLKJquiz2,
                                text="Back",command=self.MLKJquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button4a = ctk.CTkButton(master=self.page_MLKJquiz2,
                                text="Next",command=self.credits)
        button4a.grid_forget()
        radio_var3a = ctk.IntVar(master=self.page_MLKJquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_MLKJquiz2,
            text="The Maori are sigma", value=1, variable=radio_var3a,
                                                    command=MLKJButtobA)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_MLKJquiz2,
            text="I like Maccas", value=2,variable=radio_var3a,
                                                    command=MLKJButtobA)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)

        
        
        #Black Hole Quiz Page 1
        def BlackHButton():
            if radio_var2.get() == 1:
                button3.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button3.grid_forget()
        label = ctk.CTkLabel(self.page_blackhquiz1,
                text="What is a black hole?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_blackhquiz1,
                                text="Back",command=self.Blackhole)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button3 = ctk.CTkButton(master=self.page_blackhquiz1,
                                text="Next", command=self.Blackhquiz2)
        button3.grid_forget()
        radio_var2 = ctk.IntVar(master=self.page_blackhquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_blackhquiz1,
            text="The Maori are sigma", value=1, variable=radio_var2,
                                                        command=BlackHButton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_blackhquiz1,
            text="I like Maccas", value=2,variable=radio_var2,
                                                        command=BlackHButton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)

    #Black Hole Quiz Page 2 
        def BlackHButtonA():
            if radio_var2a.get() == 1:
                button3a.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button3a.grid_forget()
        label = ctk.CTkLabel(self.page_blackhquiz2,
                text="What is a black hole?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_blackhquiz2,
                                text="Back",command=self.Blackhquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button3a = ctk.CTkButton(master=self.page_blackhquiz2,
                                text="Next", command=self.credits)
        button3a.grid_forget()
        radio_var2a = ctk.IntVar(master=self.page_blackhquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_blackhquiz2,
            text="The Maori are sigma", value=1, variable=radio_var2a,
                                                        command=BlackHButtonA)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_blackhquiz2,
            text="I like Maccas", value=2,variable=radio_var2a,
                                                        command=BlackHButtonA)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        

        #Trinity Test Quiz Page 1
        def Trinitybutton():
            if radio_var1.get() == 1:
                button2.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button2.grid_forget()
        label = ctk.CTkLabel(self.page_trinityquiz1,
            text="What is the Trimity test?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_trinityquiz1,
                                text="Back",command=self.Trinity)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button2 = ctk.CTkButton(master=self.page_trinityquiz1,
                                text="Next", command=self.Trinityquiz2)
        button2.grid_forget()
        radio_var1 = ctk.IntVar(master=self.page_trinityquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_trinityquiz1,
            text="The Maori are sigma", value=2, variable=radio_var1,
                                                    command=Trinitybutton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_trinityquiz1,
            text="I like Maccas", value=1,variable=radio_var1,
                                                    command=Trinitybutton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        
    #Trinity Test Quiz Page 2
        def TrinitybuttonA():
            if radio_var1a.get() == 1:
                button2a.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button2a.grid_forget()
        label = ctk.CTkLabel(self.page_trinityquiz2,
            text="What is the Trimity test?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_trinityquiz2,
                                text="Back",command=self.Trinityquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button2a = ctk.CTkButton(master=self.page_trinityquiz2,
                                text="Next", command=self.credits)
        button2a.grid_forget()
        radio_var1a = ctk.IntVar(master=self.page_trinityquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_trinityquiz2,
            text="The Maori are sigma", value=2, variable=radio_var1a,
                                                    command=TrinitybuttonA)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_trinityquiz2,
            text="I like Maccas", value=1,variable=radio_var1a,
                                                    command=TrinitybuttonA)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)

        
        #Maori Wars Quiz Page 1
        def Maoributton():
            if radio_var.get() == 1:
                button1.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button1.grid_forget()
        label = ctk.CTkLabel(self.page_maoriquiz1,
            text="What were the Maori Wars?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_maoriquiz1,
                                text="Back",command=self.MaoriW)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button1 = ctk.CTkButton(master=self.page_maoriquiz1,
                                text="Next")
        button1.grid_forget()
        radio_var = ctk.IntVar(master=self.page_maoriquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_maoriquiz1,
                            text="The Maori are sigma", value=1,
                                variable=radio_var,command=Maoributton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_maoriquiz1,
            text="I like Maccas", value=2,variable=radio_var,
                                        command=Maoributton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)

    #Maori Wars Quiz Page 2
        def MaoributtonA():
            if radio_vara.get() == 1:
                button1a.grid(row = 9, column = 2,pady = 10, padx = 30)
            else:
                button1a.grid_forget()
        label = ctk.CTkLabel(self.page_maoriquiz2,
            text="What were the Maori Wars?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_maoriquiz2,
                                text="Back",command=self.Maoriwquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button1a = ctk.CTkButton(master=self.page_maoriquiz2,
                                text="Next", command=self.credits)
        button1a.grid_forget()
        radio_vara = ctk.IntVar(master=self.page_maoriquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_maoriquiz2,
                            text="The Maori are sigma", value=1,
                                variable=radio_vara,command=MaoributtonA)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_maoriquiz2,
            text="I like Maccas", value=2,variable=radio_vara,
                                        command=MaoributtonA)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)


    #Credits Page
        label = ctk.CTkLabel(self.page_credits, text="Credits",
            font=("Harlow Solid Italic",100))
        label.grid(row = 0, column = 1, columnspan = 1,pady = 60, padx = 60)
        label = ctk.CTkLabel(self.page_credits, text="Made by: Matthew Carter")
        label.grid(row = 1, column = 1,pady = 60, padx = 60)
        label = ctk.CTkLabel(self.page_credits, text="Version: 1.0")
        label.grid(row = 2, column = 1,pady = 60, padx = 60)
        label = ctk.CTkLabel(self.page_credits, 
            text="If you would like to check out further information on the, topics in this app, please visit the following websites:")
        button = ctk.CTkButton(master=self.page_credits,text="Back to menu",
            height=60, width=120,font=("Helvetica",25), command=self.menu)
        button.grid(row = 5, column = 0,pady = 60, padx = 60)
        button = ctk.CTkButton(master=self.page_credits,text="Quit",
            height=60, width=120,font=("Helvetica",25), command=self.quit)
        button.grid(row = 5, column = 2,pady = 60, padx = 60)
 

        
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
        self.page_trinityquiz1.place_forget()
        self.page_maoriquiz1.place_forget()
        self.page_blackhquiz1.place_forget()
        self.page_japquiz1.place_forget()
        self.page_blackhquiz1.place_forget()
        self.page_volcquiz1.place_forget()
        self.page_MLKJquiz1.place_forget()
        self.page_volcquiz2.place_forget()
        self.page_blackhquiz2.place_forget()
        self.page_japquiz2.place_forget()
        self.page_trinityquiz2.place_forget()
        self.page_MLKJquiz2.place_forget()
        self.page_japquiz2.place_forget()
        self.page_credits.place_forget()
        
    
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

    def Volcquiz1(self):
        self.hide_all_pages()
        self.page_volcquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Volcquiz2(self):
        self.hide_all_pages()
        self.page_volcquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def MLKJquiz(self):
        self.hide_all_pages()
        self.page_MLKJquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def MLKJquiz2(self):
        self.hide_all_pages()
        self.page_MLKJquiz2.place(relx = 0.5, rely=0.5, anchor=tk.CENTER)

    def Blackhquiz(self):
        self.hide_all_pages()
        self.page_blackhquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Blackhquiz2(self):
        self.hide_all_pages()
        self.page_blackhquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Japquiz(self):
        self.hide_all_pages()
        self.page_japquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Japquiz2(self):
        self.hide_all_pages()
        self.page_japquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Trinityquiz(self):
        self.hide_all_pages()
        self.page_trinityquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Trinityquiz2(self):
        self.hide_all_pages()
        self.page_trinityquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def Maoriwquiz(self):
        self.hide_all_pages()
        self.page_maoriquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def Maoriwquiz2(self):
        self.hide_all_pages()
        self.page_maoriquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def settings(self):
        self.hide_all_pages()
        self.settings_page.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

    def credits(self):
        self.hide_all_pages()
        self.page_credits.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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
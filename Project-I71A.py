import customtkinter as ctk
import tkinter as tk
import wikipedia
from Text import *
import threading as thread

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the appearance mode to system and the default color theme to
        # dark-blue
        # Modes: system (default), light, dark
        ctk.set_appearance_mode("system")
        # Themes: blue (default), dark-blue, green
        ctk.set_default_color_theme("dark-blue")

        # Starts the app in fullscreen
        self.after(0, lambda: self.state('zoomed'))
        self.geometry("1920x1080")
        self.state('normal')

        self.welcome = ctk.CTkFrame(self, width=500, height=500)
        self.welcome.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.title("Project-I71A")  # Title of the app


        # Gets the pages ready but doesn't place them
        self.page_volc = ctk.CTkFrame(self)
        self.page_volcquiz1 = ctk.CTkFrame(self)
        self.page_volcquiz2 = ctk.CTkFrame(self)
        self.page_mlkj = ctk.CTkFrame(self)
        self.page_mlkjquiz1 = ctk.CTkFrame(self)
        self.page_mlkjquiz2 = ctk.CTkFrame(self)
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

        # Welcome page
        label = ctk.CTkLabel(self.welcome, text="Welcome",
            font=("Harlow Solid Italic",150))
        label.pack(pady=300,padx=500)
        label = ctk.CTkLabel(self.welcome,
            text="Empowering kids through knowledge",
              font=("Harlow Solid Italic",50))
        label.place(relx=0.5,rely=0.7, anchor=tk.CENTER)
        button = ctk.CTkButton(self.welcome, text="Next",
            command=self.menu,height=60, width=120,font=("Helvetica",25))
        button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
        button = ctk.CTkButton(self.welcome, text="Quit",    
            command=quit,height=60, width=120,font=("Helvetica",25))
        button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)
        
        # Menu page with buttons to navigate to other pages
        label = ctk.CTkLabel(self.menu_page, text="Menu",
            font=("Harlow Solid Italic",100))
        label.grid(row = 0, column = 2, columnspan = 1,pady = 60, padx = 60)
        button = ctk.CTkButton(self.menu_page, text="Volcanoes",
            command=self.volc).grid(row = 2, column = 1, pady = 40, padx = 30)
        button = ctk.CTkButton(self.menu_page, text="MLKJ",
            command=self.mlkj).grid(row = 3, column = 3, pady = 40, padx = 30)
        button = ctk.CTkButton(self.menu_page, text="Japan",
            command=self.japan).grid(row = 3, column = 1, pady = 40, padx = 30)
        button = ctk.CTkButton(self.menu_page, text="Black holes",
            command=self.blackhole).grid(row = 2, column = 2, pady =40, padx=30)
        button = ctk.CTkButton(self.menu_page, text="Trinity test",
            command=self.trinity).grid(row = 3, column = 2, pady = 40, padx =30)
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
        
        # Volcanoes
        label = ctk.CTkLabel(self.page_volc,
            text=split_string(wikipedia.summary("volcanoes",
            sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_volc,
                text="Back",height=60, width=120,font=("Helvetica",25),
                                                    command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_volc,
                text="Next", height=60, width=120,font=("Helvetica",25),
                                                    command=self.volcquiz1)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        # Martin Luther King Junior
        label = ctk.CTkLabel(self.page_mlkj,
            text=split_string(wikipedia.summary("MLKJ",
            sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_mlkj,
                text="Back",height=60, width=120,font=("Helvetica",25),
                                                    command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_mlkj,
                text="Next",height=60,width=120,font=("Helvetica",25),
                                                    command=self.mlkjquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        # Japan culture
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
                                                    command=self.japquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        # Black hole
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
                                                    command=self.blackhquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        # Trinity test
        label = ctk.CTkLabel(self.page_trinity,
            text=split_string(wikipedia.summary("Trinity test",
            sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_trinity,
                text="Back",height=60, width=120,font=("Helvetica",25),
                command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_trinity,
                text="Next",height=60, width=120,font=("Helvetica",25),
                command=self.trinityquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        #Maori Wars
        label = ctk.CTkLabel(self.page_maoriw,
            text=split_string(wikipedia.summary("Maori Wars",
            sentences = 10), 150), font=("Helvetica",25),height=500, width= 10)
        label.pack(pady=100,padx = 20)
        button = ctk.CTkButton(master=self.page_maoriw,
                text="Back",height=60, width=120,font=("Helvetica",25),
                command=self.menu)
        button.place(relx=0.2, rely=0.9, anchor=ctk.S)
        button = ctk.CTkButton(master=self.page_maoriw,
                text="Next",height=60, width=120,font=("Helvetica",25),
                command=self.maoriwquiz)
        button.place(relx=0.8, rely=0.9, anchor=ctk.S)

        # Volc Quiz Page 1
        def volcbutton():
            # Show button6 if the condition met
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
                                text="Next",command=self.volcquiz2)
        button6.grid_forget()
        radio_var5 = ctk.IntVar(master=self.page_volcquiz1,
                                value=0)
        # When the Value = 1, the button will show. This means that the user
        # has selected the correct answer
        my_rad1 = ctk.CTkRadioButton(master=self.page_volcquiz1,
            text="A rupture in the crust", value=1, variable=radio_var5,
                                                        command=volcbutton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_volcquiz1,
            text="A spicy hill", value=2,variable=radio_var5,command=volcbutton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_volcquiz1,
            text="A mountain", value=3,variable=radio_var5,command=volcbutton)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_volcquiz1,
            text="Hot pools", value=4,variable=radio_var5,command=volcbutton)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

        # Volc Quiz Page 2
        def volcbuttona():
            if radio_var5a.get() == 1:
                button6a.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button6a.grid_forget()
        label = ctk.CTkLabel(self.page_volcquiz2,
                              text="What can large eruptions cause?",
                              font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_volcquiz2,
                                text="Back",command=self.volcquiz1)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button6a = ctk.CTkButton(master=self.page_volcquiz2,
                                text="Next",command=self.credits)
        button6a.grid_forget()
        radio_var5a = ctk.IntVar(master=self.page_volcquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_volcquiz2,
            text="Animal behaviour", value=4, variable=radio_var5a,
                                                        command=volcbuttona)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_volcquiz2,
            text="The economy", value=2,variable=radio_var5a,
            command=volcbuttona)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_volcquiz2,
            text="The ocean's current", value=3,variable=radio_var5a,
            command=volcbuttona)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_volcquiz2,
            text="Atmospheric temperature",
            value=1,variable=radio_var5a,command=volcbuttona)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)
      
        # Japanese Quiz Page 1
        def japbutton():
            if radio_var4.get() == 1:
                button5.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button5.grid_forget()
        label = ctk.CTkLabel(self.page_japquiz1,
                            text="Which groups helped shape Japanese Culture?",
                            font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_japquiz1,
                                text="Back",command=self.japan)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button5 = ctk.CTkButton(master=self.page_japquiz1,
                                text="Next",command=self.japquiz2)
        button5.grid_forget()
        radio_var4 = ctk.IntVar(master=self.page_japquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_japquiz1,
            text="Sakai", value=2, variable=radio_var4, command=japbutton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_japquiz1,
            text="Yayoi", value=1,variable=radio_var4,command=japbutton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_japquiz1,
            text="Han", value=3,variable=radio_var4,command=japbutton)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_japquiz1,
            text="Nara", value=4,variable=radio_var4,command=japbutton)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

        # Japanese Quiz Page 2
        def japbuttona():
            if radio_var4a.get() == 1:
                button5a.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button5a.grid_forget()
        label = ctk.CTkLabel(self.page_japquiz2,
                        text="After how many years did Japan open itself to" 
                        "Western influences?",
                        font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_japquiz2,
                                text="Back",command=self.japquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button5a = ctk.CTkButton(master=self.page_japquiz2,
                                text="Next",command=self.credits)
        button5a.grid_forget()
        radio_var4a = ctk.IntVar(master=self.page_japquiz2, value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_japquiz2,
                            text="573 Years", value=4,
                            variable=radio_var4a,command=japbuttona)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_japquiz2,
                            text="987 Years", 
                            value=2, variable=radio_var4a,command=japbuttona)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton (master=self.page_japquiz2,
                            text="214 Years", 
                            value=3, variable=radio_var4a,command=japbuttona)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_japquiz2,text="220 Years",
        value=1,variable=radio_var4a,command=japbuttona)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)


        # MLKJ Quiz Page 1
        def mlkjbutton():
            if radio_var3.get() == 1:
                button4.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button4.grid_forget()
        label = ctk.CTkLabel(self.page_mlkjquiz1,
                              text="Who was Martin Luther King Junior?"
                              ,font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_mlkjquiz1,
                                text="Back",command=self.mlkj)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button4 = ctk.CTkButton(master=self.page_mlkjquiz1,
                                text="Next",command=self.mlkjquiz2)
        button4.grid_forget()
        radio_var3 = ctk.IntVar(master=self.page_mlkjquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_mlkjquiz1,
            text="A German Priest", value=2, variable=radio_var3,
                                                    command=mlkjbutton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_mlkjquiz1,
            text="An American Civil Rights Activist",
              value=1,variable=radio_var3,command=mlkjbutton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_mlkjquiz1,
            text="One of the Founding Fathers of the USA",
            value=3,variable=radio_var3,command=mlkjbutton)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)   
        my_rad4 = ctk.CTkRadioButton(master=self.page_mlkjquiz1,
            text="A spy for the US Army", value=4,variable=radio_var3,
                                                    command=mlkjbutton)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)
    
        # MLKJ Quiz Page 2
        def mlkjbuttona():
            if radio_var3a.get() == 1:
                button4a.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button4a.grid_forget()
        label = ctk.CTkLabel(self.page_mlkjquiz2,
                    text="What was Martin Luther King Junior's iconic saying?",
                    font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_mlkjquiz2,
                                text="Back",command=self.mlkjquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button4a = ctk.CTkButton(master=self.page_mlkjquiz2,
                                text="Next",command=self.credits)
        button4a.grid_forget()
        radio_var3a = ctk.IntVar(master=self.page_mlkjquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_mlkjquiz2,
            text="I have a dream", 
            value=1, variable=radio_var3a, command=mlkjbuttona)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_mlkjquiz2,
            text="The unexamined life is not worth living",
              value=2,variable=radio_var3a, command=mlkjbuttona)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_mlkjquiz2,
            text="Make America great again",
            value=3,variable=radio_var3a, command=mlkjbuttona)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_mlkjquiz2,
            text="Knowledge makes a man unfit to be a slave",
            value=4,variable=radio_var3a,command=mlkjbuttona)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)


        # Black Hole Quiz Page 1
        def blackhbutton():
            if radio_var2.get() == 1:
                button3.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button3.grid_forget()
        label = ctk.CTkLabel(self.page_blackhquiz1,
                text="What is a black hole?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_blackhquiz1,
                                text="Back",command=self.blackhole)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button3 = ctk.CTkButton(master=self.page_blackhquiz1,
                                text="Next", command=self.blackhquiz2)
        button3.grid_forget()
        radio_var2 = ctk.IntVar(master=self.page_blackhquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_blackhquiz1,
            text="A portal to another universe", value=2, variable=radio_var2,
                                                        command=blackhbutton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_blackhquiz1,
            text="An unescapable region of spacetime", 
            value=1,variable=radio_var2,command=blackhbutton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_blackhquiz1,
            text="A wormhole", value=3,variable=radio_var2,
                                                        command=blackhbutton)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_blackhquiz1,
            text="A star", value=4,variable=radio_var2,command=blackhbutton)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

        # Black Hole Quiz Page 2 
        def blackhbuttona():
            if radio_var2a.get() == 1:
                button3a.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button3a.grid_forget()
        label = ctk.CTkLabel(self.page_blackhquiz2,
                text="What can you do with a black hole?",
                font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_blackhquiz2,
                                text="Back",command=self.blackhquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button3a = ctk.CTkButton(master=self.page_blackhquiz2,
                                text="Next", command=self.credits)
        button3a.grid_forget()
        radio_var2a = ctk.IntVar(master=self.page_blackhquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_blackhquiz2,
            text="Taste it", value=3, variable=radio_var2a,
                                                        command=blackhbuttona)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_blackhquiz2,
            text="Touch it", value=2,variable=radio_var2a,
                                                        command=blackhbuttona)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_blackhquiz2,
            text="Smell it", value=4,variable=radio_var2a,
                                                        command=blackhbuttona)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_blackhquiz2,
            text="Study it", value=1,variable=radio_var2a,
                                                        command=blackhbuttona)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

        # Trinity Test Quiz Page 1
        def trinitybutton():
            if radio_var1.get() == 1:
                button2.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button2.grid_forget()
        label = ctk.CTkLabel(self.page_trinityquiz1,
            text="What is the Trinity test?",font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_trinityquiz1,
                                text="Back",command=self.trinity)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button2 = ctk.CTkButton(master=self.page_trinityquiz1,
                                text="Next", command=self.trinityquiz2)
        button2.grid_forget()
        radio_var1 = ctk.IntVar(master=self.page_trinityquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_trinityquiz1,
            text="An experiment that split a hydrogen atom",
              value=2, variable=radio_var1,command=trinitybutton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_trinityquiz1,
            text="The first detonation of a nuclear bomb",
            value=1,variable=radio_var1, command=trinitybutton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_trinityquiz1,
            text="A test to see if the world is round",
            value=3,variable=radio_var1, command=trinitybutton)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_trinityquiz1,
            text="The first car that was powered by 3 types of fuel",
            value=4,variable=radio_var1, command=trinitybutton)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)
        
        # Trinity Test Quiz Page 2
        def TrinitybuttonA():
            if radio_var1a.get() == 1:
                button2a.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button2a.grid_forget()
        label = ctk.CTkLabel(self.page_trinityquiz2,
            text="Who was the experiment assigned to?",
            font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_trinityquiz2,
                                text="Back",command=self.trinityquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button2a = ctk.CTkButton(master=self.page_trinityquiz2,
                                text="Next", command=self.credits)
        button2a.grid_forget()
        radio_var1a = ctk.IntVar(master=self.page_trinityquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_trinityquiz2,
            text="Ernest Rutherford", value=3, variable=radio_var1a,
                                                    command=TrinitybuttonA)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_trinityquiz2,
            text="Albert Einstein", value=2,variable=radio_var1a,
                                                    command=TrinitybuttonA)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_trinityquiz2,
            text="J. Robert Oppenheimer", value=1,variable=radio_var1a,
                                                    command=TrinitybuttonA)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_trinityquiz2,
            text="Marie Curie", value=4,variable=radio_var1a,
                                                    command=TrinitybuttonA)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

        # Maori Wars Quiz Page 1
        def Maoributton():
            if radio_var.get() == 1:
                button1.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button1.grid_forget()
        label = ctk.CTkLabel(self.page_maoriquiz1,
            text="How did the Maori Wars start?",
            font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_maoriquiz1,
                                text="Back",command=self.MaoriW)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button1 = ctk.CTkButton(master=self.page_maoriquiz1,
                                text="Next", command=self.maoriwquiz2)
        button1.grid_forget()
        radio_var = ctk.IntVar(master=self.page_maoriquiz1,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_maoriquiz1,
                            text="Over a loaf of bread", value=2,
                                variable=radio_var,command=Maoributton)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_maoriquiz1,
            text="Tension over land purchases", value=1,variable=radio_var,
                                        command=Maoributton)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_maoriquiz1,
            text="A disagreement over a horse", value=3,variable=radio_var,
                                        command=Maoributton)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_maoriquiz1,
            text="Mistranslation in sacred texts", value=4,variable=radio_var,
                                        command=Maoributton)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

        # Maori Wars Quiz Page 2
        def MaoributtonA():
            if radio_vara.get() == 1:
                button1a.grid(row = 9, column = 3,pady = 10, padx = 30)
            else:
                button1a.grid_forget()
        label = ctk.CTkLabel(self.page_maoriquiz2,
            text="How many Maori were killed in the wars?",
            font=("Harlow Solid Italic",50))
        label.grid(row = 0, column = 1, columnspan = 2,pady = 60, padx =120)
        button = ctk.CTkButton(master=self.page_maoriquiz2,
                                text="Back",command=self.maoriwquiz)
        button.grid(row = 9, column = 0,pady = 10, padx = 30)
        button1a = ctk.CTkButton(master=self.page_maoriquiz2,
                                text="Next", command=self.credits)
        button1a.grid_forget()
        radio_vara = ctk.IntVar(master=self.page_maoriquiz2,
                                value=0)
        my_rad1 = ctk.CTkRadioButton(master=self.page_maoriquiz2,
                            text="2100+", value=1,
                                variable=radio_vara,command=MaoributtonA)
        my_rad1.grid(row=1,column=1,pady = 10, padx = 30)
        my_rad2 = ctk.CTkRadioButton(master=self.page_maoriquiz2,
            text="7900+", value=2,variable=radio_vara,
                                        command=MaoributtonA)
        my_rad2.grid(row=3,column=1,pady = 10, padx = 30)
        my_rad3 = ctk.CTkRadioButton(master=self.page_maoriquiz2,
            text="1000+", value=3,variable=radio_vara,
                                        command=MaoributtonA)
        my_rad3.grid(row=1,column=2,pady = 10, padx = 30)
        my_rad4 = ctk.CTkRadioButton(master=self.page_maoriquiz2,
            text="500+", value=4,variable=radio_vara,
                                        command=MaoributtonA)
        my_rad4.grid(row=3,column=2,pady = 10, padx = 30)

        # Credits Page
        label = ctk.CTkLabel(self.page_credits, text="Credits",
            font=("Harlow Solid Italic",100))
        label.grid(row = 0, column = 1, columnspan = 1,pady = 60, padx = 60)
        label = ctk.CTkLabel(self.page_credits,
                        text="Made by: Matthew Carter")
        label.grid(row = 4, column = 1, padx = 60, pady = 20)
        label = ctk.CTkLabel(self.page_credits, text="Version: 1.0")
        label.grid(row = 9, column = 1,pady = 20, padx = 60)
        label = ctk.CTkLabel(self.page_credits, 
            text="If you would like to check out further information on the " 
            "topics in this app, please check out \n"
            "Wikipedia or any relevant sources " 
            "regarding each topic", font=("Helvetica",25))
        label.grid(row = 1, column = 1,pady = 20, padx = 60)
        label = ctk.CTkLabel(self.page_credits,
            text="Thank you for participating :)\n"
            "Further updates will be provided to bring more questions,"
              " articles and a more improved version", font=("Helvetica",25))
        label.grid(row = 2, column = 1,pady = 20, padx = 60)
        label = ctk.CTkLabel(self.page_credits,
            text="Thanks to my teachers, friends and family for their support")
        label.grid(row = 5, column = 1, padx = 60, pady = 20)
        button = ctk.CTkButton(master=self.page_credits,text="Back to Menu",
            height=60, width=120,font=("Helvetica",25), command=self.menu)
        button.grid(row = 9, column = 0,pady = 60, padx = 60)
        button = ctk.CTkButton(master=self.page_credits,text="Quit",
            height=60, width=120,font=("Helvetica",25), command=self.quit)
        button.grid(row = 9, column = 2,pady = 60, padx = 60)

        # Settings Page
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
    
    # Hide all pages when switching between them
    def hide_all_pages(self):
        self.welcome.place_forget()
        self.page_volc.place_forget()
        self.page_mlkj.place_forget()
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
        self.page_mlkjquiz1.place_forget()
        self.page_volcquiz2.place_forget()
        self.page_blackhquiz2.place_forget()
        self.page_japquiz2.place_forget()
        self.page_trinityquiz2.place_forget()
        self.page_mlkjquiz2.place_forget()
        self.page_japquiz2.place_forget()
        self.page_maoriquiz2.place_forget()
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
        
    def mlkj(self):
        self.hide_all_pages()
        self.page_mlkj.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def japan(self):
        self.hide_all_pages()
        self.page_jap.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def blackhole(self):
        self.hide_all_pages()
        self.page_blackh.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def trinity(self):
        self.hide_all_pages()
        self.page_trinity.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def MaoriW(self):
        self.hide_all_pages()
        self.page_maoriw.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def volcquiz1(self):
        self.hide_all_pages()
        self.page_volcquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def volcquiz2(self):
        self.hide_all_pages()
        self.page_volcquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def mlkjquiz(self):
        self.hide_all_pages()
        self.page_mlkjquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def mlkjquiz2(self):
        self.hide_all_pages()
        self.page_mlkjquiz2.place(relx = 0.5, rely=0.5, anchor=tk.CENTER)

    def blackhquiz(self):
        self.hide_all_pages()
        self.page_blackhquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def blackhquiz2(self):
        self.hide_all_pages()
        self.page_blackhquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def japquiz(self):
        self.hide_all_pages()
        self.page_japquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def japquiz2(self):
        self.hide_all_pages()
        self.page_japquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def trinityquiz(self):
        self.hide_all_pages()
        self.page_trinityquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def trinityquiz2(self):
        self.hide_all_pages()
        self.page_trinityquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def maoriwquiz(self):
        self.hide_all_pages()
        self.page_maoriquiz1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def maoriwquiz2(self):
        self.hide_all_pages()
        self.page_maoriquiz2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def settings(self):
        self.hide_all_pages()
        self.settings_page.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

    def credits(self):
        self.hide_all_pages()
        self.page_credits.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Changes the appearance of the app
    def dark_mode(self):
        ctk.set_appearance_mode("dark")

    def light_mode(self):
        ctk.set_appearance_mode("light")

if __name__ == "__main__":
    app = App()
    app.mainloop()
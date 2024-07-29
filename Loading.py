import threading as thread
import customtkinter as ctk
import wikipedia

loaded_websites = {}
website = [
    'volcanoes',
    'MLKJ',
    'Japanese Culture',
]

class Thread(thread.Thread):
    def __init__(self, website_name: str):
        super().__init__()
        loaded_websites[website_name] = wikipedia.summary(website_name)

    def run(self):
        pass

class Loading(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue") 

        self.after(0, lambda: self.state('zoomed'))
        self.geometry("1920x1080")
        self.state('normal')

        self.loading_frame = ctk.CTkFrame(self, width=100, height=100)
        self.loading_frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)

    def load_website_async(self):
        pass

    def loading_thing(self):
        pass

if __name__ == "__main__":
    Loading().mainloop()
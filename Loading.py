import threading as thread, customtkinter as ctk, wikipedia

loaded_websites = {}

class Thread(thread.Thread):
    def __init__(self, website_name: str):
        super().__init__()
        self.website = website_name

    def run(self):
        loaded_websites[self.website] = wikipedia.summary(self.website)

class Loading(ctk.CTk):
    websites = [
        'volcanoes',
        'MLKJ',
        'Japanese Culture',
    ]

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue") 


        self.geometry("100x100")
        
        self.state('normal')

        self.loading_frame = ctk.CTkFrame(self, width=100, height=100)
        self.loading_frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)

        for website_data in enumerate(self.websites):
            self.load_website_async(website_data)

    def load_website_async(self, website_data):
        index, website = list(website_data)
        Thread(website).start()

    def loading_thing(self):
        pass

if __name__ == "__main__":
    Loading().mainloop()
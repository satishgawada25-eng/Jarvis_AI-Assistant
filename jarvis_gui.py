import customtkinter as ctk
from PIL import Image
import psutil
import threading
import time
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class JarvisHUD:

    def __init__(self):

        self.app = ctk.CTk()
        self.app.geometry("900x600")
        self.app.title("JARVIS AI SYSTEM")

        title = ctk.CTkLabel(self.app,text="JARVIS AI INTERFACE",font=("Arial",28))
        title.pack(pady=20)

        image = Image.open("assets/ai_girl.png.webp")

        avatar = ctk.CTkImage(light_image=image,size=(250,350))

        self.avatar = ctk.CTkLabel(self.app,image=avatar,text="")
        self.avatar.pack(pady=10)

        self.time_label = ctk.CTkLabel(self.app,text="")
        self.time_label.pack()

        self.cpu_label = ctk.CTkLabel(self.app,text="CPU")
        self.cpu_label.pack()

        self.ram_label = ctk.CTkLabel(self.app,text="RAM")
        self.ram_label.pack()

        self.log = ctk.CTkTextbox(self.app,width=600,height=200)
        self.log.pack(pady=20)

        threading.Thread(target=self.update_stats,daemon=True).start()

    def update_stats(self):

        while True:

            now = datetime.now().strftime("%H:%M:%S")

            cpu = psutil.cpu_percent()

            ram = psutil.virtual_memory().percent

            self.time_label.configure(text=f"TIME : {now}")
            self.cpu_label.configure(text=f"CPU : {cpu}%")
            self.ram_label.configure(text=f"RAM : {ram}%")

            time.sleep(1)

    def add_log(self,text):

        self.log.insert("end",text+"\n")

    def run(self):

        self.app.mainloop()


if __name__ == "__main__":

    hud = JarvisHUD()

    hud.add_log("Jarvis system online")
    hud.add_log("AI assistant ready")

    hud.run()
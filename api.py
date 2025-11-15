import tkinter as tk
import requests
import customtkinter as ct

#Definujeme funkce
def get_position():
    response=requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    latitude=data["iss_position"]["latitude"]
    longitude=data["iss_position"]["longitude"]
    longitudelabel.configure(text=f"Zeměpisná délka ISS je: {longitude}")
    latitudelabel.configure(text=f"Zeměpisná šířka ISS je {latitude}")
    latitudelabel.pack()
    longitudelabel.pack()

#Okno
window=ct.CTk()
window.geometry("500x600")
window.resizable(False, False)
window.title("Pozice ISS")

#Canvas
canvas=tk.Canvas(window, width=400, height=224)
canvas.pack()
img=tk.PhotoImage(file="iss.gif")
canvas.create_image(0, 0, anchor="nw", image=img)

#Přepočítávací tlačítko
button1=ct.CTkButton(window, text="Zjistit souřadnice ISS", command=get_position)
button1.pack()

#Label
latitudelabel=ct.CTkLabel(window)
longitudelabel=ct.CTkLabel(window)

#Hlavní cyklus
window.mainloop()
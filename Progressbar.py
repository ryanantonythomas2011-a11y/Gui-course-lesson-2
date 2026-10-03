from tkinter import*
from tkinter.ttk import*
import time
screen = Tk()
screen.geometry("500x400")
screen.config(background="Purple")
progress_bar = Progressbar(screen,orient="horizontal",length=300)

def progressupdate():
    progress_bar["value"] = 20
    screen.update_idletasks()
    time.sleep(1) 

    progress_bar["value"] = 40
    screen.update_idletasks()
    time.sleep(1) 

    progress_bar["value"] = 60
    screen.update_idletasks()
    time.sleep(1) 
    
    progress_bar["value"] = 80
    screen.update_idletasks()
    time.sleep(1) 

    progress_bar["value"] = 100
    screen.update_idletasks()
    time.sleep(1) 


progress_bar.place(x=60,y=40)
start = Button(screen,text="Start",command=progressupdate).place(x=60,y=100)
mainloop()

from tkinter import*
from tkinter.ttk import*
import time 
screen = Tk()
screen.title("Restaurant")
screen.geometry("600x500")
screen.config(background="Violet")

email = Label(screen,text="Email").place(x=40,y=30)
email_box = Entry(screen,width=35).place(x=140,y=30)
password = Label(screen,text="Password").place(x=40,y=70)
password_box = Entry(screen,show = "*", width=35).place(x=140,y=70)

mains = Label(screen,text="What food would you like: Chicken Sandwich,BLT,Veg Sandwich or None?").place(x=40,y=130)
mains_box  = Entry(screen,width=35).place(x=40,y=160)
spinbox1 = Spinbox(screen,from_=1,to=20).place(x=40,y=180)

drinks = Label(screen,text="What beverage would you like: Cola,Fanta,Orange Juice,Water or None?").place(x=40,y=210)
drinks_box  = Entry(screen,width=35).place(x=40,y=240)
spinbox2 = Spinbox(screen,from_=1,to=20).place(x=40,y=260)

dessert = Label(screen,text="What desert would you like: An Ice cream, an ice lolly ,chocolate cake or None?").place(x=40,y=290)
desert_box  = Entry(screen,width=35).place(x=40,y=320)
spinbox3 = Spinbox(screen,from_=1,to=20).place(x=40,y=340)

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


progress_bar.place(x=250,y=400)
start = Button(screen,text="Submit",command=progressupdate).place(x=250,y=350)

mainloop()




from tkinter import*
screen = Tk()
screen.geometry("500x500")
screen.config(background="violet")

listbox = Listbox(screen,width=20,height=15)
listbox.insert(1,"space")
listbox.insert(2,"earth")
listbox.insert(3,"Sun")
listbox.insert(4,"ocean")
listbox.pack()
mainloop()

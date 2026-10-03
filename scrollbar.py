from tkinter import*
screen = Tk()
screen.geometry("500x500")
screen.config(background="violet")

scrollbar = Scrollbar(screen)
scrollbar.pack(side=LEFT,fill=Y)
listbox = Listbox(screen,height=50,width=50,yscrollcommand=scrollbar.set)
for i in range(1,100):
    listbox.insert(END,i)
listbox.pack(side=RIGHT,fill=BOTH)
scrollbar.config(command=listbox.yview)
mainloop()
    
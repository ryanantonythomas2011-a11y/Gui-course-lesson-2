from tkinter import*
screen = Tk()
screen.geometry("500x500")
screen.config(background="violet")

top_frame = Frame(screen,bg="crimson",width=100,height=100)
top_frame.pack()
bottom_frame = Frame(screen,bg="crimson",width=100,height=100)
bottom_frame.pack(side=BOTTOM)
topframe_button = Button(top_frame,text="Click")
bottomframe_button = Button(bottom_frame,text="Click here")
topframe_button.pack(side=LEFT)
bottomframe_button.pack()
leftframe_button = Button(top_frame,text="click")
leftframe_button.pack(side=RIGHT)
rightframe_button = Button(bottom_frame,text="click")
rightframe_button.pack(side=BOTTOM)

mainloop()

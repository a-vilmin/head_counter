import tkinter

def hello():
    s = enter.get()
    print("Hello "+ s)

top = tkinter.Tk()
top.title("Head Count Email")

lbl = tkinter.Label(top, text= "How many people tonight?")
enter = tkinter.Entry(top)
btn = tkinter.Button(top, text= "Send Email", command=hello)

lbl.pack()
enter.pack()
btn.pack()


top.mainloop()



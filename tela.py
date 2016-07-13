from Tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text="Hello World")
        self.msg.pack()
        self.bye = Button(self, text="Bye", command=self.quit)
        self.bye.pack()
        self.pack()
app = Application()
app.master.title("Controle Financeiro")
app.master.geometry('400x200+100+100')
mainloop()

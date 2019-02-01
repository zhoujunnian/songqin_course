# coding
from Tkinter import *
import tkMessageBox

class myFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master,width=500,height=500)
        self.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

root = Tk()

root.title('Hello World')

root.mainloop()
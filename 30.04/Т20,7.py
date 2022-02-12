from collections import defaultdict
from tkinter import *
from tkinter.messagebox import *


class Vector():

    def __init__(self):
        self.first = Tk()
        #self.
        
        self.n = input('n =')
        self.components = defaultdict()
        self.top = Tk()
        for i in range(self.n):
            Label(self.top, text = 'v{} ='.format(i),
                    font=('arial', 16)).pack(side=LEFT) 
            Q = Entry(self.top)
            self.components['v'+str(i)] = Q.get()
        self.top.mainloop()

    def IsEmpty(self):
        for i in self.components.values():
            if i == '':
                messagebox.showerror('Error', 'Не введено число')
    

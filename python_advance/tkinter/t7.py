from tkinter import *
class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title('Menu Demo')
        
        menubar = Menu(window)
        window.config(menu = menubar)
        
        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = 'operation', menu = operationMenu)
        operationMenu.add_command(label = 'add', command = self.add)
        operationMenu.add_command(label = 'subtract', command = self.subtract)
        operationMenu.add_command(label = 'mutiply', command = self.mutiply)
        operationMenu.add_command(label = 'divide', command = self.divide)
        
        exitmenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = 'exit', menu = exitmenu)
        exitmenu.add_command(label = 'quit', command = window.quit)
        
        frame1 = Frame(window)
        frame1.grid(row = 1, column = 1, pady = 10)
        Label(frame1, text = 'number1:').pack(side = LEFT)
        self.v1 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v1, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text = 'number2:').pack(side = LEFT)
        self.v2 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v2, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text = 'result:').pack(side = LEFT)
        self.v3 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v3, justify = RIGHT
        ).pack(side = LEFT)
        
        frame2 = Frame(window)
        frame2.grid(row = 2, column = 1, pady = 10)
        Button(frame2, text = 'add', command = self.add).pack(side = LEFT)
        Button(frame2, text = 'subtract', command = self.subtract).pack(side = LEFT)
        Button(frame2, text = 'mutiply', command = self.mutiply).pack(side = LEFT)
        Button(frame2, text = 'divide', command = self.divide).pack(side = LEFT)
        
        mainloop()
        
    def add(self):
        self.v3.set(eval(self.v1.get()) + eval(self.v2.get()))
            
    def subtract(self):
        self.v3.set(eval(self.v1.get()) - eval(self.v2.get()))
            
    def mutiply(self):
        self.v3.set(eval(self.v1.get()) * eval(self.v2.get()))
            
    def divide(self):
        self.v3.set(eval(self.v1.get()) / eval(self.v2.get()))
            
MenuDemo()

        
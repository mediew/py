from tkinter import *
class PackManageDemo:
    def __init__(self):
        window = Tk()
        window.title('pack manage')
        
        Label(window, text = 'blue', bg = 'blue').pack()
        Label(window, text = 'red', bg = 'red').pack(fill = \
            BOTH, expand = 1)
        Label(window, text = 'green', bg = 'green').pack( \
            fill = BOTH)
        
        window.mainloop()
        
PackManageDemo()
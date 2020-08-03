from tkinter import *
class GridManageDemo:
    window = Tk()
    window.title('Grid Manage')
    
    message = Message(window, text = "this message occupies three \
        rows and two column")
    message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2) 
    Label(window, text = 'first name').grid(row = 1, column = 3)
    Entry(window).grid(row = 1, column = 4, padx = 5, pady = 5)
    Label(window, text = 'last name').grid(row = 2, column = 3)
    Entry(window).grid(row = 2, column = 4, padx = 5, pady = 5)
    Button(window, text = 'get name').grid(row = 3, padx = 5, \
        pady = 5, column = 4, sticky = E)
        
    window.mainloop()
GridManageDemo()
from tkinter import *
from random import *

class MoveBall:
    def __init__(self):
        window = Tk()
        window.title('Move a Ball')
        
        self.width = 200
        self.height = 200
        self.canvas = Canvas(window, width = self.width, height = self.height)
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
        Button(frame, text = 'left', command = self.left).pack(side = LEFT)
        Button(frame, text = 'right', command = self.right).pack(side = LEFT)
        Button(frame, text = 'up', command = self.up).pack(side = LEFT)
        Button(frame, text = 'down', command = self.down).pack(side = LEFT)
        
        self.x, self.y = randint(0, 200), randint(0, 200)
        self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill = 'black', tags = 'ball')
        
        self.d = 5
        
        window.mainloop()

    '''
    def isOver(self):
        if self.x > 190 or self.y > 190:
            isOver = True
    '''
        
    def left(self):
        self.canvas.move('ball', -self.d, 0)
        #self.canvas.update()
        
    def right(self):
        self.canvas.move('ball', self.d, 0)
        
    def up(self):
        self.canvas.move('ball', 0, -self.d)
        
    def down(self):
        self.canvas.move('ball', 0, self.d)
        
MoveBall()
        
        
        
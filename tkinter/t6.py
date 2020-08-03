from tkinter import *
class ImageDemo:
    def __init__(self):
        window = Tk()
        window.title('Image Demo')
        
        caImage = PhotoImage(file = 'image/ca.gif')
        chinaImage = PhotoImage(file = 'image/china.gif')
        leftImage = PhotoImage(file = 'image/left.gif')
        rightImage = PhotoImage(file = 'image/right.gif')
#        usImage = PhotoImage(file = 'image/us.gif')
#        ukImage = PhotoImage(file = 'image/uk.gif')
        crossImage = PhotoImage(file = 'image/x.gif')
        circleImage = PhotoImage(file = 'image/o.gif')
        
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, image = caImage).pack(side = LEFT)
        canvas = Canvas(frame1)
        canvas.create_image(90, 50, image = chinaImage)
        canvas['width'] = 200
        canvas['height'] = 100
        canvas.pack(side = LEFT)
        
        frame2 = Frame(window)
        frame2.pack()
        Button(frame2, image = leftImage).pack(side = LEFT)
        Button(frame2, image = rightImage).pack(side = LEFT)
#        Checkbutton(frame2, image = ukImage).pack(side = LEFT)
        Radiobutton(frame2, image = crossImage).pack(\
            side = LEFT)
        Radiobutton(frame2, image = circleImage).pack(\
            side = LEFT)
        window.mainloop()

ImageDemo()
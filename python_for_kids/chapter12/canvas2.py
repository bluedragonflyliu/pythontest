from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_image = PhotoImage(file='bg.png')
canvas.create_image(0,0, image=my_image, anchor='nw')

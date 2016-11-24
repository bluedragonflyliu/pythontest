from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
mytriangle = canvas.create_polygon(10,10,10,60,50,35,fill="red")

for x in range(0,60):
    canvas.move(mytriangle,10,10)
    canvas.itemconfig(mytriangle,fill="skyblue")
    tk.update()
    time.sleep(0.5)
   
    canvas.itemconfig(mytriangle,fill="red")
    tk.update()
    time.sleep(0.5)

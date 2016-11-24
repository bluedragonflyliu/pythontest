from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
my_triangle = canvas.create_polygon(10,10,10,60,50,35)
def movetriangle(event):
    if event.keysym == "Up":
        canvas.move(my_triangle,0,-5)
        canvas.itemconfig(my_triangle,fill="red")
    elif event.keysym =="Down":
        canvas.move(my_triangle,0,5)
        canvas.itemconfig(my_triangle,fill="skyblue")
    elif event.keysym == "Left":
        canvas.move(my_triangle,-5,0)
        canvas.itemconfig(my_triangle,fill="green")
    else:
        canvas.move(my_triangle,5,0)
        canvas.itemconfig(my_triangle,fill="pink")
#canvas.bind_all("<KeyPress-Return>", movetriangle)
canvas.bind_all("<KeyPress-Up>", movetriangle)
canvas.bind_all("<KeyPress-Down>", movetriangle)
canvas.bind_all("<KeyPress-Left>", movetriangle)
canvas.bind_all("<KeyPress-Right>", movetriangle)


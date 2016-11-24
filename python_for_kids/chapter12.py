from tkinter import *
def say():
    print("hello python")
tk = Tk()
btn = Button(tk,text="click me", command=say)
btn.pack()

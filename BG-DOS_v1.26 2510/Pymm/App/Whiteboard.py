from tkinter import *
import tkinter as tk


def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    c.create_oval(x1, y1, x2, y2, fill = 'black', outline = 'black')

def eraser(event):
    x1, y1 = (event.x - 40), (event.y - 40)
    x2, y2 = (event.x + 40), (event.y + 40)
    c.create_oval(x1, y1, x2, y2, fill = 'white', outline = 'white')

def clear(event):
    c.delete(tk.ALL)

root = tk.Tk()
root.title('Pymm Whiteboard')
c = Canvas(root, width = 800, height = 600, bg = 'white')
c.pack(expand = YES, fill = BOTH)
c.bind("<B1-Motion>", paint)
c.bind("<B2-Motion>", clear)
c.bind("<B3-Motion>", eraser)

mess = Label(root, text = '拖动鼠标左键画东西, 拖动鼠标右键橡皮, 鼠标中键清屏')
mess.pack(side = BOTTOM)

root.mainloop()
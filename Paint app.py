# Paint app "Artist Studio"
# import relevant libraries
from tkinter import *

# globals
lastx, lasty = 0, 0
color = "black"

# functions
def xy(event):
	global lastx, lasty
	lastx, lasty = event.x, event.y

def setColor(newcolor):
	global color
	color = newcolor

def addLine(event):
	global lastx, lasty
	canvas.create_line((lastx, lasty, event.x, event.y), fill = color, width = 30)
	lastx, lasty = event.x, event.y

# root create + setup
root = Tk()
root.geometry('800x580')
root.title('Artist Studio')
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

# canvas create + setup
canvas = Canvas(root)
canvas.grid(column = 0, row = 0, sticky = (N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
# setting up the color menu
id = canvas.create_rectangle((10, 10, 30, 30), fill = "#000000")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#000000"))
id = canvas.create_rectangle((10, 35, 30, 55), fill = "#141923")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#141923"))
id = canvas.create_rectangle((10, 60, 30, 80), fill = "#414168")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#414168"))

id = canvas.create_rectangle((10, 85, 30, 105), fill = "#3a7fa7")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#3a7fa7"))
id = canvas.create_rectangle((10, 110, 30, 130), fill = "#35e3e3")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#35e3e3"))
id = canvas.create_rectangle((10, 135, 30, 155), fill = "#8fd970")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#8fd970"))

id = canvas.create_rectangle((10, 160, 30, 180), fill = "#5ebb49")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#5ebb49"))
id = canvas.create_rectangle((10, 185, 30, 205), fill = "#458352")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#458352"))
id = canvas.create_rectangle((10, 210, 30, 230), fill = "#dcd37b")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#dcd37b"))

id = canvas.create_rectangle((10, 235, 30, 255), fill = "#fffcc7")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#fffcc7"))
id = canvas.create_rectangle((10, 260, 30, 280), fill = "#ffd035")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#ffd035"))
id = canvas.create_rectangle((10, 285, 30, 305), fill = "#cc9245")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#cc9245"))

id = canvas.create_rectangle((10, 310, 30, 330), fill = "#a15c3e")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#a15c3e"))
id = canvas.create_rectangle((10, 335, 30, 355), fill = "#a42f3b")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#a42f3b"))
id = canvas.create_rectangle((10, 360, 30, 380), fill = "#f45b7a")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#f45b7a"))

id = canvas.create_rectangle((10, 385, 30, 405), fill = "#c24998")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#c24998"))
id = canvas.create_rectangle((10, 410, 30, 430), fill = "#570861")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#570861"))
id = canvas.create_rectangle((10, 435, 30, 455), fill = "#af69ed")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#af69ed"))
id = canvas.create_rectangle((10, 460, 30, 480), fill = "#e1d9d1")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#e1d9d1"))




id = canvas.create_rectangle((35, 10, 55, 30), fill = "#000030")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#000030"))
id = canvas.create_rectangle((35, 35, 55, 55), fill = "#141953")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#141953"))
id = canvas.create_rectangle((35, 60, 55, 80), fill = "#414198")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#414198"))

id = canvas.create_rectangle((35, 85, 55, 105), fill = "#3a7fd7")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#3a7fd7"))
id = canvas.create_rectangle((35, 110, 55, 130), fill = "#98e9f3")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#98e9f3"))
id = canvas.create_rectangle((35, 135, 55, 155), fill = "#8ff990")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#8ff990"))

id = canvas.create_rectangle((35, 160, 55, 180), fill = "#5ebb79")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#5ebb79"))
id = canvas.create_rectangle((35, 185, 55, 205), fill = "#458382")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#458382"))
id = canvas.create_rectangle((35, 210, 55, 230), fill = "#dcd20b")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#dcd20b"))

id = canvas.create_rectangle((35, 235, 55, 255), fill = "#fffde7")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#fffde7"))
id = canvas.create_rectangle((35, 260, 55, 280), fill = "#ffd065")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#ffd065"))
id = canvas.create_rectangle((35, 285, 55, 305), fill = "#cc9275")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#cc9275"))

id = canvas.create_rectangle((35, 310, 55, 330), fill = "#a15c6e")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#a15c6e"))
id = canvas.create_rectangle((35, 335, 55, 355), fill = "#cd071e")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#cd071e"))
id = canvas.create_rectangle((35, 360, 55, 380), fill = "#f45b9a")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#f45b9a"))

id = canvas.create_rectangle((35, 385, 55, 405), fill = "#c27998")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#c27998"))
id = canvas.create_rectangle((35, 410, 55, 430), fill = "#81588a")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#81588a"))
id = canvas.create_rectangle((35, 435, 55, 455), fill = "#bcb0c2")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#bcb0c2"))
id = canvas.create_rectangle((35, 460, 55, 480), fill = "#ffffff")
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("#ffffff"))

# main loop
root.mainloop()

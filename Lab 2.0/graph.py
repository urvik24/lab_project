# Embedding the graphs in tkinter window

from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# Creating tkinter window
win = Tk()

# Creating Figure.
fig = Figure(figsize=(10,10))

x = ["7 April","8 April","9 April","10 April","11 April","12 April","13 April"]
y = ["10","12","7","12","9","13","6"]

# Plotting the graph inside the Figure
a = fig.add_subplot(111)
a.plot(x,y, marker = "o", label = "October")
a.set_xlabel("Marks")
a.set_ylabel("Students")
a.set_title("Graph_Tk")
a.legend()
a.grid()


# Creating Canvas
canv = FigureCanvasTkAgg(fig, master = win)
canv.draw()

get_widz = canv.get_tk_widget()
get_widz.pack()

win.mainloop()

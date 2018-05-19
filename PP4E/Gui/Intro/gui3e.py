import sys
from tkinter import *


def hello(event):
    print('Press twice to exit')


def quit(event):
    print('Hello, I must be going...')
    sys.exit()


widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Button-2>', quit)
widget.mainloop()
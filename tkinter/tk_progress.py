import tkinter as tk
from tkinter import ttk

root = tk.Tk()

val = 0

def func_next():
    global val
    val += 10
    progress.configure(value=val)

def func_reset():
    global val
    val = 0
    progress.configure(value=val)

progress = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress.configure(maximum=100, value=val)
progress.pack()
button1 = tk.Button(root, text="next", command=func_next).pack()
button2 = tk.Button(root, text="reset", command=func_reset).pack()

root.mainloop()
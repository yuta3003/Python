import tkinter as tk

root = tk.Tk()

def func():
    root.quit()

def over_func(ev):
    button.config(text = 'クリックして!')

def release_func(ev):
    button.config(text = '終了')

label = tk.Label( root, text='サンプル')
label.pack()

button = tk.Button(root, text='終了', command=func)

button.bind('<Enter>', over_func)
button.bind('<Leave>', release_func)

button.pack()
root.mainloop()
import tkinter as tk

root = tk.Tk()

# チェック状態を格納する領域を確保
val1 = tk.BooleanVar()
val2 = tk.BooleanVar()

# 未チェック状態に設定
val1.set(False)
val2.set(False)

# チェックボックスの作成
chk1 = tk.Checkbutton(root, text="項目1", variable=val1)
chk1.pack()

chk2 = tk.Checkbutton(root, text="項目2", variable=val2)
chk2.pack()

def func():
    if (val1.get() and val2.get()):
        label.config(text="真真")
    elif (not(val1.get()) and val2.get()):
        label.config(text="偽真")
    elif (val1.get() and not(val2.get())):
        label.config(text="真偽")
    else:
        label.config(text="偽偽")
    pass

button = tk.Button(root, text='終了', command=func)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
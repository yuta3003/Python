import tkinter as tk

#メインウィンドウの生成
root = tk.Tk()

#ラベルの生成
label = tk.Label(root, text="ボタン1")

#ラベルの配置
label.pack()

sel = tk.IntVar()

sel.set(1)

def func1():
    pass
def func2():
    pass

rb1 = tk.Radiobutton( root, text = "ボタン 1", variable = sel, value = 1, command = func1 )

rb1.pack()

rb2 = tk.Radiobutton( root, text = "ボタン 2", variable = sel, value = 2, command = func2 )

rb2.pack()

root.mainloop()
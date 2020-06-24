import tkinter as tk

root = tk.Tk()
def func(i):
    def x():
        print(i)
    return x
for i in range(3):
    # ボタン生成と同時に配置
    tk.Button(root, text=i, command = func(i)).pack()
root.mainloop()
 # i = 0~2で、3回の繰返し処理


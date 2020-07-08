import hashlib
import tkinter as tk

root = tk.Tk()
root.geometry("400x80")

# ハッシュ関数
def safty_password(ev):
    strings = e.get()
    strings = strings.encode()
    hash = hashlib.sha256()
    hash.update(strings)
    label.config(text=hash.hexdigest())

# ボタン生成時何もしないことを宣言
def f():
    pass


# テキストボックスを配置
e = tk.Entry(root, width=400)
e.pack()

# ボタンを生成
button_hash = tk.Button(root, text='ハッシュ化', command=f)
button_hash.bind('<Button-1>', safty_password)
button_hash.pack()

# ラベルを生成
label = tk.Label(root, text="")
label.pack()

root.mainloop()
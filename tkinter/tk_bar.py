import tkinter as tk

#メインウィンドウの生成
root = tk.Tk()

# スライドバーの値を格納する場所を生成 
val = tk.IntVar()
#valに0を代入 
val.set(0)
# スライドバーを動かしたときの処理 
def func(scl):
    scl_val = int(scl)
    scl_2 = int(bin(scl_val))
    scl_10 = scl_val
    # Lavelの表示を変更
    label_val.config(text='Value = %d' % scl_val)
    label_2.config(text='%d' % scl)
    label_10.config(text='%d' % scl)

label_val = tk.Label(root, text='Value = %d' % val.get())
label_val.pack()

# スライドバーの値を表示するラベルを生成 2進数
label_2 = tk.Label(root, text='%d' % val.get())
label_2.pack()

# スライドバーの値を表示するラベルを生成 10進数
label_10 = tk.Label(root, text='%d' % val.get())
label_10.pack()
# スライドバーの生成
s = tk.Scale(   
    root, 
    label='Scale',
    orient='h',
    from_=0,
    to=32,
    showvalue=False,
    variable=val,
    command=func
)
s.pack()

root.mainloop()
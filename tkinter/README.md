# tkinter

## メイン画面作成
```py
root = tk.Tk()
root.mainloop()
```

## ラベル
```py
label = tk.Label(root, text='サンプル')
label.pack()
```

## ボタン
```py
def func():
    pass
button = tk.Button(root, text='終了', command=func)
button.pack()
```

## テキストボックス
```py
textbox = tk.Entry(root)
textbox.pack()
```

## ラジオボタン
```py
sel = tk.IntVar()
sel.set(1)

def func1():
    pass
def func2():
    pass

rbutton1 = tk.Radiobutton(root, text="ボタン 1", variable=sel, value=1, command=func1)
rbutton1.pack()

rbutton2 = tk.Radiobutton(root, text="ボタン 2", variable=sel, value=2, command=func2)
rbutton2.pack()
```

## スライドバー
```py
# スライドバーの値を格納する場所を生成 
val = tk.IntVar()
#valに0を代入 
val.set(0)
# スライドバーを動かしたときの処理 
def func(scl):
    # Lavelの表示を変更
    label.config(text='Value=%d' % int(scl))

# スライドバーの値を表示するラベルを生成
label = tk.Label(root, text='Value=%d' % val.get())
label.pack()

# スライドバーの生成
s = tk.Scale(
    root,
    label='Scale',
    orient='h',
    from_=0,
    to=100,
    showvalue=False,
    variable=val,
    command=func
)

s.pack()
```
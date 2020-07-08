import tkinter as tk

root = tk.Tk()

# キャンバスを生成 
cv = tk.Canvas(root, width=500, height=500)
cv.pack()

# 円を描画
cv.create_oval(100, 200, 150, 250, fill='black')
cv.create_oval(150, 200, 200, 250, fill='black')
cv.create_oval(200, 200, 250, 250, fill='black')

def func_blue():    
    cv.create_oval(100, 200, 150, 250, fill='blue')

def func_yellow():    
    cv.create_oval(150, 200, 200, 250, fill='yellow')

def func_red():    
    cv.create_oval(200, 200, 250, 250, fill='red')



buttonblue = tk.Button(root, text='青', command=func_blue)
buttonblue.pack()

buttonyellow = tk.Button(root, text='黄', command=func_yellow)
buttonyellow.pack()

buttonred = tk.Button(root, text='赤', command=func_red)
buttonred.pack()

root.mainloop()
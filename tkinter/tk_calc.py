import tkinter as tk

root = tk.Tk()

answer = []
def func(i):
    def x():
        answer.append(i)

    return x

def func_clear():
    e.delete(0, tk.END)
    answer.clear()
    
def func_plus():
    keep = "+"
    answer.append(keep)

def func_minus():
    keep = "-"
    answer.append(keep)

def func_equal():
    answer.append("=")
    keep = 0
    keep_list = []
    for q in range(len(answer)):
        if answer[q] == "+":
            keep_list.append(keep)
            keep_list.append("+")
            keep = 0
        elif answer[q] == "-":
            keep_list.append(keep)
            keep_list.append("-")
            keep = 0
        elif answer[q] == "=":
            keep_list.append(keep)
        else:
            keep = str(keep)
            a = str(answer[q])
            keep += a
            keep = int(keep)
        q += 1
    
    kotae = ""
    for w in range(len(keep_list)):
        kotae += str(keep_list[w])
    
    kotae = eval(kotae)
    e.insert(0, kotae)



for i in range(10):
    tk.Button(root,text=i,command=func(i)).grid(column=i, row=0)
tk.Button(root,text='+',command=func_plus).grid(column=0, row=1)
tk.Button(root,text='-',command=func_minus).grid(column=1, row=1)
tk.Button(root,text='=',command=func_equal).grid(column=2, row=1)
tk.Button(root,text='C',command=func_clear).grid(column=3, row=1)

e = tk.Entry(root)
e.grid( columnspan=10, rows=2, sticky=tk.W + tk.E)

root.mainloop()


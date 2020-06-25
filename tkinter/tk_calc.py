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
    answer.append("+")

def func_minus():
    answer.append("-")

def func_equal():
    answer.append("=")
    # answerリストから数字と式に修正する
    keep = 0
    keep_list = []
    for num in range(len(answer)):
        if answer[num] == "+":
            keep_list.append(keep)
            keep_list.append("+")
            keep = 0
        elif answer[num] == "-":
            keep_list.append(keep)
            keep_list.append("-")
            keep = 0
        elif answer[num] == "=":
            keep_list.append(keep)
        else:
            keep = str(keep)
            ans = str(answer[num])
            keep += ans
            keep = int(keep)

    # 計算結果表示部
    display_ans = ""
    for kl in range(len(keep_list)):
        display_ans += str(keep_list[kl])
    
    display_ans = eval(display_ans)
    e.insert(0, display_ans)



for i in range(10):
    tk.Button(root,text=i,command=func(i)).grid(column=i, row=0)
tk.Button(root,text='+',command=func_plus).grid(column=0, row=1)
tk.Button(root,text='-',command=func_minus).grid(column=1, row=1)
tk.Button(root,text='=',command=func_equal).grid(column=2, row=1)
tk.Button(root,text='C',command=func_clear).grid(column=3, row=1)

e = tk.Entry(root)
e.grid( columnspan=10, rows=2, sticky=tk.W + tk.E)

root.mainloop()


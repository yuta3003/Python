import tkinter as tk

root = tk.Tk()
root.title('Listboxテスト')

def listbox_selected(ev):
    e.delete(0, tk.END)
    e.insert(tk.END, lb.get(lb.curselection()))

listdata = ('大村', '田嶋', '山本')
v1 = tk.StringVar(value = listdata)
lb = tk.Listbox(root, listvariable = v1, height = 4)
lb.bind('<<ListboxSelect>>', listbox_selected)
lb.pack()
# テキストボックス
e = tk.Entry( root )
e.pack()
root.mainloop()
import tkinter as tk

#メインウィンドウの生成
root = tk.Tk()

keep = 0



# スライドバーの値を格納する場所を生成 
val = tk.IntVar()
#valに0を代入 
val.set(0)
# スライドバーを動かしたときの処理 
def func(scl):
# Lavelの表示を変更
    label1.config( text = 'Value = %d' % int(scl))
    global keep
    keep = val.get()
    test(keep)

# スライドバーの値を表示するラベルを生成
label1 = tk.Label(root, text = 'Value = %d' % val.get())
label1.pack()

label2 = tk.Label(root,text="")
label2.pack()

label3 = tk.Label(root,text="")
label3.pack()

#label2の表示
def test(a):
    keep = a
    ans = "00000000000000000000000000000000"
    ans = list(ans)
    for i in range(keep):
        ans[i] = "1"
        i+=1
    mojiretu=""
    for q in range(len(ans)):
        if (q == 8) or (q == 16) or (q == 24) or (q == 32):
            mojiretu += "."
        mojiretu += ans[q]
        q+=1
    mojiretu 
    label2.config(text=mojiretu)

    ans10_1 = mojiretu[0: 8]
    ans10_2 = mojiretu[9: 17]
    ans10_3 = mojiretu[18: 26]
    ans10_4 = mojiretu[27: 35]

    # print(ans10_1)
    # print(ans10_2)
    # print(ans10_3)
    # print(ans10_4)

    ans1 = str(int(ans10_1, 2))
    ans2 = str(int(ans10_2, 2))
    ans3 = str(int(ans10_3, 2))
    ans4 = str(int(ans10_4, 2))

    # print(ans1)
    # print(ans2)
    # print(ans3)
    # print(ans4)

    # text3_1 = int(ans10_1, 2)
    # text3_2 = int(ans10_2, 2)
    # text3_3 = int(ans10_3, 2)
    # text3_4 = int(ans10_4, 2)

    text3mojiretu = ans1+"."+ans2+"."+ans3+"."+ans4

    label3.config(text=text3mojiretu)

    

    # print(ans10_1)
    # print(ans10_2)
    # print(ans10_3)
    # print(ans10_4)

    # for l in range

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
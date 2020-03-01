# -*- coding: utf-8 -*-
import random

nextNo = random.randint(1, 100)
count = 0
while True:
    preNo = nextNo
    print("HIGH OR LOW? :" + str(preNo))

    #  入力値をH or L に限定
    while True:
        userAns = input("(H/L)")
        print(userAns[0])
        if (userAns[0] == "H" or userAns[0] == "L"):
            break
    
    nextNo = random.randint(1, 100)
    print(nextNo)

    if preNo < nextNo:
        answer = "H"
        print("HIGH")
    elif preNo == nextNo:
        continue
    else:
        answer = "L"
        print("LOW")

    if answer == userAns:
        count = count + 1
        print("正解数：" + str(count))
    else:
        print("残念！")
        break



import random

correct_answer_no = 0   # 正解数カウント

rNo = random.random()   # 0~1
rNo = round(rNo * 100 + 1)  # 1~100
next_rNo = rNo

while True:
    print(rNo)

    while (next_rNo == rNo):     # next_rNo生成部 next_rNo != rNo となるように生成
        next_rNo = random.random()
        next_rNo = round(next_rNo * 100 + 1)

    # print(next_rNo)   # 確認用
    while True:     # answer入力部 入力値チェック
        response = input("High or Low?[high/low]:")
        if response == "h" or response == "high" or response == "l" or response == "low":
            break
        else:
            print("入力値エラー")
            print("[high or low]のみ入力可能です。")

    if ((response == "h" or response == "high") and rNo < next_rNo):
        correct_answer_no += 1
    elif ((response == "l" or response == "low") and rNo > next_rNo):
        correct_answer_no += 1
    else:
        break

    rNo = next_rNo

print("正解数は{}".format(correct_answer_no))


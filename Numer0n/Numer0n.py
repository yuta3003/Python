import random
import sys

while True:
    nextGame = 0
    question_no = [
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9)
    ]
    while (question_no[0] == question_no[1]):
        question_no[1] = random.randint(0,9)
    while (question_no[0] == question_no[2] or question_no[1] == question_no[2]):
        question_no[2] = random.randint(0,9)
    while (question_no[0] == question_no[3] or question_no[1] == question_no[3] or question_no[2] == question_no[3]):
        question_no[3] = random.randint(0,9)

    count = 0
    print("*****************************************")
    print("        welcome to the game              ")
    print("*****************************************")
    while True:
        hit = 0
        blow = 0
        count += 1
        while True:
            answer = input("4桁の数字を入力してください:")
            if len(answer) != 4:           # 桁数チェック
                print("桁数エラー")
                continue
            if len(answer) != len(set(answer)): # 被りがないかチェック
                print("入力値エラー")
                continue
            print(answer)
            break

        for i in range(4):
            for j in range(4):
                if i == j and int(question_no[i]) == int(answer[j]):
                    hit += 1
                elif i != j and int(question_no[i]) == int(answer[j]):
                    blow += 1
    
        print("hit:{}".format(str(hit)))
        print("blow:{}".format(str(blow)))

        if hit == 4:
            print("*****************************************")
            print("          you win the game               ")
            print("*****************************************")
            print("回数:{}".format(str(count)))
            sys.exit()
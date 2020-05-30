import random
import sys


def main():
    nextGame = 0
    question_no = create_question()
    print(question_no)

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
            return 0


def create_question():
    create_no = [
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9),
        random.randint(0, 9)
    ]
    while (create_no[0] == create_no[1]):
        create_no[1] = random.randint(0,9)
    while (create_no[0] == create_no[2] or create_no[1] == create_no[2]):
        create_no[2] = random.randint(0,9)
    while (create_no[0] == create_no[3] or create_no[1] == create_no[3] or create_no[2] == create_no[3]):
        create_no[3] = random.randint(0,9)

    return create_no


if __name__ == '__main__':
    main()
    sys.exit()
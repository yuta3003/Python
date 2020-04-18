import os

def main():
    horizontal_line = []
    max_length = 0

    while True:
        file_name = input("対象ファイル名を入力してください:")
        if os.path.isfile(file_name):
            break
        print("ファイル名エラー")
        
    with open(file_name,'r') as read_file:
        for row in read_file:
            row = row.replace('\n','')
            horizontal_line.append(row)

    for i in range(len(horizontal_line)):
        if len(horizontal_line[i]) > max_length:
            max_length = len(horizontal_line[i])

    for i in range(len(horizontal_line)):
        horizontal_line[i] = horizontal_line[i].ljust(max_length)

    for i in range(len(horizontal_line[1])): # 文字数分ループ
        test = ""
        for j in reversed(range(len(horizontal_line))): # 要素数分リバースループ
            test += horizontal_line[j][i] + " "
        print(test)

if __name__=='__main__':
    main()
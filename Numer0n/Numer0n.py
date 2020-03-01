# -*- coding: utf-8 -*-

import random
import sys

while True:
  nextGame = 0
  a = [
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9),
    random.randint(0, 9)
  ]
  # 乱数生成
  while (a[0] == a[1]):
    a[1] = random.randint(0,9)
  while (a[0] == a[2] or a[1] == a[2]):
    a[2] = random.randint(0,9)
  while (a[0] == a[3] or a[1] == a[3] or a[2] == a[3]):
    a[3] = random.randint(0,9)
  count =0
  print("*****************************************")
  print("        welcome to the game              ")
  print("*****************************************")
  while True:
    hit = 0
    blow = 0
    count +=1
    while True:
      y = input("4桁の数字を入力してください:")
      if len(y) != 4:           # 桁数チェック
        print("桁数エラー")
        continue
      if len(y) != len(set(y)): # 被りがないかチェック
        print("入力値エラー")
        continue
      print(y)
      break

    for i in range(4):
      for j in range(4):
        if i == j and int(a[i]) == int(y[j]):
          hit += 1
        elif i != j and int(a[i]) == int(y[j]):
          blow += 1
    
    print("hit:{}".format(str(hit)))
    print("blow:{}".format(str(blow)))

    if hit == 4:
      print("*****************************************")
      print("          you win the game               ")
      print("*****************************************")
      print("回数:{}".format(str(count)))
      sys.exit()




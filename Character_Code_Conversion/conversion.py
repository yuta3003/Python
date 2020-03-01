# -*- coding:utf-8 -*-
import codecs
import sys

args = sys.argv

def main():
  shiftjis_path = args[1] # 変換元のファイルパス
  utf8_path = args[2]     # 出力先のファイルパス

  # 文字コードを utf-8 に変換して保存
  fin = codecs.open(shiftjis_path, "r", "shift_jis")
  fout_utf = codecs.open(utf8_path, "w", "utf-8")
  for row in fin:
    fout_utf.write(row)
  fin.close()
  fout_utf.close()

if __name__ == '__main__':
  main()

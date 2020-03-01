import os
import sys
import difflib

args = sys.argv

def main():
    file1_name = args[1]
    file2_name = args[2]
    print(diff(file1_name, file2_name))

def diff(file_name1, file_name2):
    f1 = open(file_name1, 'r')
    f2 = open(file_name2, 'r')
    d = difflib.Differ()
    diff = d.compare(f1.readlines(), f2.readlines())
    return '\n'.join(diff)

if __name__ == '__main__':
    main()

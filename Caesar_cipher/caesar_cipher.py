"""
3文字ずらし
TODO:複数ずらしに対応
"""
import string

encrypted_string = input("シーザー暗号を入力:")

# encrypt = string.ascii_lowercase + string.ascii_uppercase
encrypt = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
decrypt = "xyzabcdefghijklmnopqrstuvwXYZABCDEFGHIJKLMNOPQRSTUVW"

for i in range(len(enctypeted_string)):
    decrypted_string = encrypted_string.replace(encrypt[i], decrypt[i])

print(test1)
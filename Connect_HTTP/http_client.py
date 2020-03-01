import requests
"""
pip install requests

HTTPにリクエストを送信して情報を取得する
"""

url = 'http://www.google.com/'
response = requests.get(url)    # HTTPリクエストを送信しレスポンスを取得

INDENT = '    '

print("HTTPリクエスト情報")
print("{}[リクエストURL{}]".format(INDENT, url))
"""
GET / HTTP/1.1
Host: www.google.com
User-Agent: curl/7.54.0
Accept: */*
"""

print("HTTPレスポンス情報")
print("{}[ステータスコード:{}]".format(INDENT, response.status_code))
print("{}[ステータスメッセージ{}]".format(INDENT, response.reason))
# print("{}[ヘッダ情報{}]".format(INDENT, response.headers))
# print(response.text)
# http://www.pythonchallenge.com/pc/def/ocr.html
from urllib import request

def insert_char(dic, char):
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1

dic = dict()
chars = str()
text = str()

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
with request.urlopen(url) as response:
    html = response.read().decode('utf-8')
    chars = html.split('<!--')[-1].split('-->')[0]

for char in chars:
    insert_char(dic, char)

for char in chars:
    if dic[char] == 1:
        print(char, end='')

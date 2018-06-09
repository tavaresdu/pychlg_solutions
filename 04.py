# http://www.pythonchallenge.com/pc/def/linkedlist.php
from urllib import request
import re

nothing = 12345

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

while(True):
    with request.urlopen(url + '?nothing=' + str(nothing)) as response:
        text = response.read().decode('utf-8')
        print(text)
        match = re.search(r'next nothing is (\d+)', text, re.MULTILINE)
        if match is not None:
            nothing = int(match.group(1))
        elif 'Divide by two' in text:
            nothing = nothing // 2
        elif 'html' in text:
            break

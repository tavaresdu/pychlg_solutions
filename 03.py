from urllib import request
import re

text = str()

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
with request.urlopen(url) as response:
    html = response.read().decode('utf-8')
    text = html.split('<!--')[-1].split('-->')[0]

filtered = str()

for match in re.finditer(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text):
    filtered += match.group(1)

print(filtered)

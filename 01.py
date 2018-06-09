# http://www.pythonchallenge.com/pc/def/map.html
from bs4 import BeautifulSoup
from urllib import request
import string

intab = string.ascii_lowercase
outtab = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
transtab = str.maketrans(intab, outtab)

url = 'http://www.pythonchallenge.com/pc/def/map.html'
with request.urlopen(url) as response:
    html = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
    text = html.find('font', color='#f000f0').get_text()
    print(text.translate(transtab))

print(url.split('/')[-1].split('.')[0].translate(transtab))

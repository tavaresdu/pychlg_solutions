import requests
import zipfile
import io
import re

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'

r = requests.get(url)
zipf = zipfile.ZipFile(io.BytesIO(r.content))
info = zipf.infolist()
files = {f.filename: (zipf.read(f), f.comment) for f in info}
zipf.close()

m = re.search(r'start from (\d+)', str(files['readme.txt'][0]))
number = m.group(1)

while m:
    print(files[number+'.txt'][1].decode('utf-8'), end='')
    number = m.group(1)
    text = files[number+'.txt'][0].decode('utf-8')
    m = re.search(r'Next nothing is (\d+)', text)

print()

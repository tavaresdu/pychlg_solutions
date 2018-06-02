from PIL import Image
from io import BytesIO
import requests

url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

response = requests.get(url)
image = Image.open(BytesIO(response.content))
size = image.size

chars = []
previous = None
for i, pixel in enumerate(list(image.getdata())):
    if i % size[0] == 0 or previous is not None:
        if pixel[0] == pixel[1] == pixel[2]:
            if previous != pixel:
                chars.append(pixel[0])
            previous = pixel
        elif previous is not None:
            break

text = ''.join(chr(char) for char in chars)
lst = text.split('[')[1].split(']')[0].split(', ')
nxt = ''.join(chr(int(char)) for char in lst)

print(text.split('[')[0] + nxt.replace('\n', '\\n'))

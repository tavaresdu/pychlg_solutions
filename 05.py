# http://www.pythonchallenge.com/pc/def/peak.html
from urllib import request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

with request.urlopen(url) as response:
    obj = pickle.loads(response.read())

    for line in obj:
        for char, quant in line:
            for i in range(quant):
                print(char, end='')
        print()

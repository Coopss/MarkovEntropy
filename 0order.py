import math
from util import importText

#   PKZIP: 63.5%

def convertCountToProbability(d):
    total = sum(d.values())
    p = {}
    for k,v in d.items():
        p.update({k : v/total})

    return p

def computeBitsNeeded(p):
    bits = 0
    for k,v in p.items():
        bits += - v * math.log2(v)
    return bits

def computeH0(text):
    d = {}
    for c in text:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    p = convertCountToProbability(d)
    return computeBitsNeeded(p)

if __name__ == '__main__':
    text = importText("texts/english/warandpeace_1.txt")
    print('H0 for text: ' + str(computeH0(text)))
    text = importText("texts/gujarati/warandpeace_1.en.gu.txt")
    print('H0 for text: ' + str(computeH0(text)))

    # with open('images/jpg/landscape.jpg', 'rb') as f:
    #     print('H0 for image: ' + str(computeH0(f)))
    # with open('images/bmp/landscape.bmp', 'rb') as f:
    #     print('H0 for image: ' + str(computeH0(f)))
    # with open('images/png/landscape.png', 'rb') as f:
    #     print('H0 for image: ' + str(computeH0(f)))

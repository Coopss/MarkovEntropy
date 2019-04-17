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
    d = {}
    text = importText("ulysses.txt")
    print('H0 for text: ' + str(computeH0(text)))
    text = importText("warandpeace.txt")
    print('H0 for text: ' + str(computeH0(text)))

    with open('image.jpg', 'rb') as f:
        print('H0 for image: ' + str(computeH0(f)))

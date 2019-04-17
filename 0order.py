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

if __name__ == '__main__':
    d = {}
    text = importText("warandpeace.txt")
    for c in text:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1


    p = convertCountToProbability(d)
    print(d)
    print(p)
    print(computeBitsNeeded(p))

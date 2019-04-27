import math
from util import importText

class ZOrder():
    def __init__(self, text):
        self.text = text

    def build(self):
        self.d = {}
        for c in self.text:
            if c not in self.d:
                self.d[c] = 1
            else:
                self.d[c] += 1
        self.convertCountToProbability()
        return

    def convertCountToProbability(self):
        total = sum(self.d.values())
        self.p = {}
        for k,v in self.d.items():
            self.p.update({k : v/total})
        return

    def computeBitsNeeded(self):
        bits = 0
        for k,v in self.p.items():
            bits += - v * math.log2(v)
        return bits

    def computeH0(self):
        return self.computeBitsNeeded()

if __name__ == '__main__':
    text = importText("texts/english/warandpeace.txt")
    m = ZOrder(text.lower())
    m.build()
    print('H0 for text: ' + str(m.computeH0()))


    # print('H0 for text: ' + str(computeH0(text)))

    # with open('images/jpg/landscape.jpg', 'rb') as f:
    #     print('H0 for image: ' + str(computeH0(f)))
    # with open('images/bmp/landscape.bmp', 'rb') as f:
    #     print('H0 for image: ' + str(computeH0(f)))
    # with open('images/png/landscape.png', 'rb') as f:
    #     print('H0 for image: ' + str(computeH0(f)))

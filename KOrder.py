from util import importText
from pprint import pprint
from math import log2
import re

class Markov():
    def __init__(self, text, order = 1, isImage=False):
        self.isImage = isImage
        self.text = text
        self.order = order
        self.d = {}
        self.p = {}
        self.X = {} # substring dict

    def build(self):
        for word in self.window():
            if (len(word) == self.order + 1):
                if (self.isImage):
                    chars = bytearray(word)
                else:
                    chars = list(word)
                try:
                    if (self.isImage):
                        self.d[bytes(chars[-1])][bytes(chars[:-1])] += 1
                    else:
                        self.d[chars[-1]][''.join(chars[: len(chars) - 1])] += 1
                except:
                    try:
                        if (self.isImage):
                            self.d[bytes(chars[-1])].update({bytes(chars[:-1]) : 1})
                        else:
                            self.d[chars[-1]].update({''.join(str(x) for x in chars[: len(chars) - 1]) : 1})
                    except:
                        if (self.isImage):
                            self.d.update({bytes(chars[-1]) : {}})
                            self.d[bytes(chars[-1])].update({bytes(chars[:-1]) : 1})
                        else:
                            self.d.update({chars[-1] : {}})
                            self.d[chars[-1]].update({''.join(str(x) for x in chars[: len(chars) - 1]) : 1})

        self.convertToP()

    def convertToP(self):
        for k,v in self.d.items():
            c = 0
            self.p.update({k: {}})
            for count in v.values():
                c += count

            for prefix, count in v.items():
                self.p[k].update({prefix : count / c})

        return self.p

    def window(self):
        for i in range(len(self.text) - self.order + 2):
            yield self.text[i : i + self.order + 1]

    def computeSumX(self, x):
        def window(fseq, window_size):
            for i in range(len(fseq) - window_size + 1):
                yield fseq[i:i+window_size]

        if (not self.X):
            for substring in window(self.text, self.order):
                try:
                    self.X[substring] += 1
                except:
                    self.X.update({substring : 1})

        return self.X[x]

    def computeTotalCount(self):
        c = 0
        for k,v in self.d.items():
            for prefix, count in v.items():
                c += count
        return c

    def computeHk(self):
        sum = 0
        for y, v in self.d.items():
            for x, count in v.items():
                pyx = count / self.computeSumX(x)
                px = self.computeSumX(x) / self.computeTotalCount()
                sum += -log2(pyx) * pyx * px
        return sum


if __name__ == '__main__':
    # text = importText('texts/english/warandpeace.txt')
    # m = Markov(text.lower(), order = 3)
    # m.build()
    # print(m.computeSumX('e'))
    # print(m.computeTotalCount())

    with open('images/jpg/landscape.jpg', 'rb') as f:
        Markov(f.read().lower(), order = 1).build()
        print(m.computeHk())

from util import importText
from pprint import pprint
from math import log2

class Markov():
    def __init__(self, text, order = 1):
        self.text = text
        self.order = order
        self.d = {}
        self.p = {}

    def build(self):
        for word in self.window():
            if (len(word) == self.order + 1):
                chars = list(word)
                try:
                    self.d[chars[-1]][''.join(chars[: len(chars) - 1])] += 1
                except:
                    try:
                        self.d[chars[-1]].update({''.join(str(x) for x in chars[: len(chars) - 1]) : 1})
                        # self.d[chars[-1]].update({''.join(chars[: len(chars) - 1]) : 1})
                    except:
                        self.d.update({chars[-1] : {}})
                        self.d[chars[-1]].update({''.join(str(x) for x in chars[: len(chars) - 1]) : 1})
                        # self.d[chars[-1]].update({''.join(chars[: len(chars) - 1]) : 1})
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
        c = 0
        for k,v in self.d.items():
            for prefix, count in v.items():
                if (x == prefix):
                    c += count
        return c

    def computeTotalCount(self):
        c = 0
        for k,v in self.d.items():
            for prefix, count in v.items():
                c += count
        return c
    def computeH1(self):
        sum = 0
        for y, v in self.d.items():
            for x, count in v.items():
                pyx = count / self.computeSumX(x) 
                px = self.computeSumX(x) / self.computeTotalCount() 
                sum += -log2(pyx) * pyx * px
        return sum


if __name__ == '__main__':
    text = importText('texts/english/warandpeace.txt')
    m = Markov(text.lower(), order = 1)
    m.build()
    print(m.computeSumX('e'))
    print(m.computeTotalCount())
    print(m.computeH1())

    # with open('images/jpg/landscape.jpg', 'rb') as f:
    #     Markov(f.read().lower(), order = 1).build()

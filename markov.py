from util import importText
from pprint import pprint

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
                        self.d[chars[-1]].update({''.join(chars[: len(chars) - 1]) : 1})
                    except:
                        self.d.update({chars[-1] : {}})
                        self.d[chars[-1]].update({''.join(chars[: len(chars) - 1]) : 1})
        self.convertToP()

    def convertToP(self):
        for k,v in self.d.items():
            c = 0
            self.p.update({k: {}})
            for count in v.values():
                c += count

            for prefix, count in v.items():
                self.p[k].update({prefix : count / c})

        pprint(self.p)

    def window(self):
        for i in range(len(self.text) - self.order + 2):
            yield self.text[i : i + self.order + 1]

    def longestWord(self):
        l = self.text.split()
        m = 0
        for word in l:
            if (len(word) > m) :
                m = len(word)
                print('found new longest word ' + word + ' | ' + str(len(word)))




if __name__ == '__main__':
    text = importText('texts/english/warandpeace.txt')
    # text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque aliquet volutpat tincidunt. Vivamus a tempor est. Morbi arcu eros, molestie non augue vel, imperdiet lacinia turpis. Fusce malesuada ut eros quis laoreet. Mauris sodales purus et eros porttitor tincidunt. Donec blandit, lacus vitae ultrices placerat, ligula lorem molestie ex, et ultricies lectus nisi rutrum urna. Vivamus sollicitudin metus a ante imperdiet aliquet. Suspendisse pellentesque velit a vehicula faucibus. Pellentesque nisi turpis, commodo sed dui ac, ullamcorper mollis tortor.'
    Markov(text.lower(), order = 1).build()
    # Markov(text.lower()).longestWord()

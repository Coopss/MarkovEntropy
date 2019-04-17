from util import importText

class Markov():
    def __init__(self, text, order = 1):
        self.text = text
        self.order = order
        self.d = {}

    def build(self):
        for word in self.window():
            if (len(word) == self.order + 1):
                print(word)
                chars = list(word)
                try:
                    self.d[chars[-1]].update({chars[: len(chars) - 1][0] : 1})
                except:
                    self.d.update({chars[-1] : {}})
                    self.d[chars[-1]].update({''.join(chars[: len(chars) - 1]) : 1})
        print(self.d)

    def window(self):
        for i in range(len(self.text) - self.order + 2):
            yield self.text[i : i + self.order + 1]

if __name__ == '__main__':
    # text = importText('texts/english/warandpeace.txt')
    text = 'foobar'
    Markov(text, order = 2).build()

from ZOrder import ZOrder
from KOrder import Markov
from util import importText

class MarkovEntropy():
    def __init__(self, path, order):
        self.text = importText(path)
        self.order = order

        self.model = None # define global model
        if self.isZeroOrder():
            self.m = ZOrder(self.text.lower())

        else:
            self.m = Markov(self.text.lower(), order = order)


    def build(self):
        self.m.build()

    def entropy(self):
        if (self.order == 0):
            return self.m.computeH0()
        else:
            return self.m.computeHk()

    def isZeroOrder(self):
        if (self.order == 0):
            return True
        else:
            return False


if __name__ == '__main__':
    m = MarkovEntropy('images/jpg/balloons.jpg', order=0)
    m.build()
    print("Entropy: " + str(m.entropy()))

from ZOrder import ZOrder
from KOrder import Markov
from util import importText, importImage

class MarkovEntropy():
    def __init__(self, path, order, isImage=False):
        self.text = None # define placeholder
        if (isImage):
            self.text = importImage(path)
        else:
            self.text = importText(path)

        self.order = order

        self.model = None # define global model
        if self.isZeroOrder():
            self.m = ZOrder(self.text.lower())

        else:
            self.m = Markov(self.text.lower(), order = order, isImage=isImage)


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
    m = MarkovEntropy('texts/english/ulysses.txt', order=1, isImage=False)
    # m = MarkovEntropy('images/jpg/balloons.jpg', order=1, isImage=True)
    m.build()
    print("Entropy: " + str(m.entropy()))
    m.m.convertToMatrix()
    # print(m.m.d)

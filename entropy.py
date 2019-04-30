from ZOrder import ZOrder
from KOrder import Markov
from util import importText, importImage
from argparse import ArgumentParser
import sys

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
    parser = ArgumentParser()
    parser.add_argument('-o', '--order', type=int, help='Order, must be >= 0', required=True)
    parser.add_argument('-f', '--filepath', help='Path to file', required=True)
    parser.add_argument('-i', '--isImage', help='Flag to identify image file', action='store_true')
    args = parser.parse_args()

    if not (args.order >= 0):
        print('Order must be >= 0')
        sys.exit(1)

    m = MarkovEntropy(args.filepath, order=args.order, isImage=args.isImage)
    m.build()
    print(args.filepath + " %d-order entropy: " % args.order + str(m.entropy()))

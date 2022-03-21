# Write a OO program to find Euclidean Distance without using library function from numpy or scipy.
import math


class Ec:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def euclid(self):
        d = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        ans = "{:.2f}".format(d)
        print("Euclidean dist is: ", ans)


if __name__ == '__main__':
    ggs = Ec(3, 2, 4, 1)
    ggs.euclid()

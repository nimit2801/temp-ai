class Factorial:
    def __init__(self, num):
        self.num = num

    def loop_(self):
        s = 1
        for i in range(2, self.num+1):
            s *= i
        print("Factorial using loop for ", self.num, "is :", s)

    def recur(self, n):
        if n == 1:
            return 1
        else:
            return n * self.recur(n-1)


if __name__ == '__main__':
    num = 7
    ans = Factorial(num)
    ans.loop_()
    print("Recursion of ", ans.num, "is: ", ans.recur(ans.num))
import unittest
import factorial


class MyFactoTest(unittest.TestCase):
    def test1(self):
        num = 7
        ans = factorial.Factorial(num)
        self.assertEqual(ans.loop_(), 5040, "TEST GOOD FOR LOOP")

    def test2(self):
        num = 7
        ans = factorial.Factorial(num)
        self.assertEqual(ans.recur(ans.num), 5040, "TEST GOOD FOR RECURSION")


if __name__ == '__main__':
    unittest.main()

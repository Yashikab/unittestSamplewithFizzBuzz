# code in python 3.6.9
import unittest
import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    """
    FizzBuzzに関するテストを行う．
    メソッドがtestで始まるものに対してテストを行う
    """

    def __init__(self, methodName):
        super().__init__(methodName)
        self.fb = FizzBuzz.FizzBuzz()

    def test_multi3toFizz(self):
        with self.subTest(i=3):
            self.assertEqual("Fizz", self.fb.num2str(3))

    def test_multi5toBuzz(self):
        with self.subTest(i=5):
            self.assertEqual("Buzz", self.fb.num2str(5))

    def test_multi3and5toFizzBuzz(self):
        with self.subTest(num=15):
            self.assertEqual("FizzBuzz", self.fb.num2str(3*5))
        with self.subTest(num=0):
            self.assertEqual("FizzBuzz", self.fb.num2str(0))

    def test_outof3or5(self):
        with self.subTest(num=1):
            self.assertEqual("1", self.fb.num2str(1))
        with self.subTest(num=2):
            self.assertEqual("2", self.fb.num2str(2))
        with self.subTest(num=4):
            self.assertEqual("4", self.fb.num2str(4))


if __name__ == '__main__':
    unittest.main()

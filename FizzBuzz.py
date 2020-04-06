# code with python 3.6.9
# coded by yashio kabashima


class FizzBuzz():

    def num2str(self, i):
        return_str = str(i)
        if i % 3 == 0:
            return_str = "Fizz"
        if i % 5 == 0:
            return_str = "Buzz"
        if i % 3 == 0 and i % 5 == 0:
            return_str = "FizzBuzz"
        return return_str


if __name__ == '__main__':
    fb = FizzBuzz()
    for i in range(1, 101, 1):
        print(fb.num2str(i))

from multiprocessing.managers import BaseManager


class MathsClass:
    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y


class MyManager(BaseManager):
    pass

MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    with MyManager() as manager:
        maths = manager.Maths()
        print(maths.add(4, 3))         # prints 7
        print(maths.mul(7, 8))         # prints 56
from datetime import datetime
from multiprocessing import Pool, TimeoutError
import multiprocessing as mp
import time
import os


def worker_func(x):
    return x * x


def worker_func_multiparams(x, y):
    return x * y


if __name__ == '__main__':

    # start 4 worker processes
    with Pool(processes=mp.cpu_count()) as pool:

        print('apply')
        for i in range(10):
            print(pool.apply(worker_func, args=(i, ) ))
        print('\n\n')


        print('apply_async')
        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        print(res.get(timeout=1))             # prints the PID of that process
        print('\n\n')


        print('apply_async, reading the results')
        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])
        print('\n\n')


        print('apply_async with timeout')
        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")


        print('map')
        # print "[0, 1, 4,..., 81]"
        print(pool.map(worker_func, range(10)))
        print('\n\n')


        print('map_async')
        # print "[0, 1, 4,..., 81]"
        print(pool.map_async(worker_func, range(10), callback=None, error_callback=None))
        print('\n\n')


        print('imap with iterator')
        # print same numbers in arbitrary order
        results = pool.imap(worker_func, range(10))
        while True:
            try:
                result = results.next(timeout=10)
                print(result)
            except StopIteration:
                break
        print('\n\n')


        print('imap with for')
        # print same numbers in arbitrary order
        for i in pool.imap(worker_func, range(10)):
            print(i)
        print('\n\n')


        print('imap_unordered')
        # print same numbers in arbitrary order
        for i in pool.imap_unordered(worker_func, range(10)):
            print(i)
        print('\n\n')


        print('starmap')
        values = [(i, j) for i in range(4) for j in range(5)]
        print('values = {}'.format(values))
        for i in pool.starmap(worker_func_multiparams, values):
            print(i)
        print('\n\n')


        print("For the moment, the pool remains available for more work")


    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")


    print('Using Pool with context manager')
    with mp.Pool(4) as pool:
        results = pool.map(worker_func, range(10))
        for n, result in zip(range(10), results):
            print('{} {:>3} {:>10}'.format(datetime.now().time(), n, result))


    # For map()
    # Just for curiosity, if you don't set a value to the chunksize, this will be calculated this way (cpython doc):
    # https://github.com/python/cpython/blob/5affd23e6f42125998724787025080a24839266e/Lib/multiprocessing/pool.py#L378
    #
    # if chunksize is None:
    #     chunksize, extra = divmod(len(iterable), len(self._pool) * 4)
    #     if extra:
    #         chunksize += 1
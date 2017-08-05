import multiprocessing

"""
Python multiprocessing provides a manager to coordinate shared information between all its
users. A manager object controls a server process that holds Python objects and allows other
processes to manipulate them.
"""


def worker(dictionary, key, item):
    dictionary[key] = item


if __name__ == '__main__':

    # 1 - With Manager
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()

    # 1 - Withoyt Manager
    dictionary = dict()

    # Single thread
    # for i in range(10):
    #     worker(dictionary, i, i*2)

    jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i*2)) for i in range(10)]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print('Results:', dictionary)

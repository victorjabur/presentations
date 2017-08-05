from threading import Thread
import time


class Threads_object(Thread):
    def __init__(self, fnc):
        Thread.__init__(self)
        self.fnc = fnc

    def run(self):
        functions[self.fnc]()


class Nothreads_object(object):
    def __init__(self, fnc):
        Thread.__init__(self)
        self.fnc = fnc

    def run(self):
        functions[self.fnc]()


def non_threaded(num_iter, fnc):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(Nothreads_object(fnc))
    for i in funcs:
        i.run()


def threaded(num_threads, fnc):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(Threads_object(fnc))
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


def fnc_to_run_1_pass():
    pass


def fnc_to_run_2_fibonacci():
    a, b = 0, 1
    for i in range(10000):
        a, b = b, a + b


def fnc_to_run_3_file_read():
    fh = open("example.txt", "rb")
    size = 1024
    for i in range(1000):
        fh.read(size)


def fnc_to_run_4_http_request():
    import urllib.request
    with urllib.request.urlopen("http://google.com/") as f:
        f.read(1024)


def fnc_to_run_5_time_sleep():
    time.sleep(0.01)


def show_results(func_name, results):
    print ("%-23s %4.6f seconds" % (func_name, results))


if __name__ == "__main__":

    functions = [fnc_to_run_1_pass, fnc_to_run_2_fibonacci, fnc_to_run_3_file_read, fnc_to_run_4_http_request, fnc_to_run_5_time_sleep]

    import sys
    from timeit import Timer

    repeat = 5
    number = 1
    num_threads = [1, 2, 4, 8]
    print('Starting tests')

    for f in range(5):

        print("Runnnig function %s \n" % functions[f].__name__)

        for i in num_threads:
            t = Timer("non_threaded(%s, %s)" % (i, f), "from __main__ import non_threaded")
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_results("non_threaded(%s iters)" % i, best_result)

            t = Timer("threaded(%s, %s)" % (i, f), "from __main__ import threaded")
            best_result = min(t.repeat(repeat=repeat, number=number))
            show_results("threaded(%s threads) " % i, best_result)

            print('')

print('Iterations complete')
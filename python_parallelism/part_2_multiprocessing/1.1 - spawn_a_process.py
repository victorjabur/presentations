import time
import multiprocessing


def foo(arg_1):
    print('called function in process: %s' % arg_1)


if __name__ == '__main__':
    process_jobs = list()
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        process_jobs.append(p)
        p.start()
        p.join()

        time.sleep(1)
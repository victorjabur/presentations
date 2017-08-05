"""
multi_joinablequeue.py
"""
from multiprocessing import Process, JoinableQueue
import time


def reader(queue):
    while True:
        msg = queue.get()         # Read from the queue and do nothing
        queue.task_done()


def writer(count, queue):
    for ii in range(count):
        queue.put(ii)             # Write 'count' numbers into the queue


if __name__=='__main__':
    for count in [10**4, 10**5, 10**6, 10**7]:
        queue = JoinableQueue()   # reader() reads from queue
                                  # writer() writes to queue
        reader_p = Process(target=reader, args=((queue),))
        reader_p.daemon = True
        reader_p.start()     # Launch the reader process

        _start = time.time()
        writer(count, queue) # Send a lot of stuff to reader()
        queue.join()         # Wait for the reader to finish
        print("Sending %s numbers to JoinableQueue() took %s seconds" % (count, (time.time() - _start)))
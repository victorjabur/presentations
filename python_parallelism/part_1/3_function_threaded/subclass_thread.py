import threading
import time


class MyThread(threading.Thread):

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)


def print_time(thread_name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1

if __name__ == '__main__':
    # Create new threads
    thread1 = MyThread(1, "Thread-1_simple_process", 1)
    thread2 = MyThread(2, "Thread-2_class_threaded", 2)

    # Start new Threads
    thread1.start()
    thread2.start()
    print("Exiting Main Thread")
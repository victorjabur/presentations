import time
from threading import Thread, Event
import random

items = []
event = Event()


class Consumer(Thread):

    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print('Consumer notify : %d popped from list by %s' % (item, self.name))


class Producer(Thread):

    def __init__(self, integers, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        global item
        for i in range(100):
            time.sleep(2)
            item = random.randint(0, 256)
            self.items.append(item)
            print('Producer notify : item N° %d appended to list by %s' % (item, self.name))
            print('Producer notify : event set by %s' % self.name)
            self.event.set()
            print('Produce notify : event cleared by %s \n' % self.name)
            self.event.clear()

if __name__ == '__main__':

    t1 = Producer(items, event)
    t2 = Consumer(items, event)

    t2.start()
    time.sleep(1)
    t1.start()

    t1.join()
    t2.join()
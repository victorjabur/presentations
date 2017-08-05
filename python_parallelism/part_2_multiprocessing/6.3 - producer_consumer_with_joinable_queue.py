import multiprocessing
import random
import time


class Producer(multiprocessing.Process):

    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('produced: item %d appended to queue %s' % (item, self.name))
            time.sleep(1)
            print("queue size is %s" % self.queue.qsize())


class Consumer(multiprocessing.Process):

    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        time.sleep(1)

    def run(self):
        while True:
            if self.queue.empty():
                print("the queue is empty")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print('consumed : item %d popped by %s \n' % (item, self.name))
                time.sleep(1)
                print("queue size is %s" % self.queue.qsize())
                self.queue.task_done()


if __name__ == '__main__':

    queue = multiprocessing.JoinableQueue()

    process_producer = Producer(queue)
    process_consumer = Consumer(queue)

    process_producer.start()
    process_consumer.start()

    queue.join()
from multiprocessing.managers import BaseManager
import queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    queue = queue.Queue()
    QueueManager.register('get_queue', callable=lambda:queue)
    m = QueueManager(address=('', 50000), authkey=b'abracadabra')
    s = m.get_server()
    s.serve_forever()

import time
import multiprocessing


def foo():
    name = multiprocessing.current_process().name
    print('Starting %s \n' % name)
    time.sleep(2)
    print('Exiting %s \n' % name)


if __name__ == '__main__':

    process_with_name = multiprocessing.Process(name='foo_process', target=foo)

    # background execution if needed
    # a daemonic process can't spawn child process - orphan protection
    #process_with_name.daemon = True

    process_without_name = multiprocessing.Process(target=foo)

    process_with_name.start()
    process_without_name.start()


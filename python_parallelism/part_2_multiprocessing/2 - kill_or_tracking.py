import multiprocessing
import time


def foo():
    print('Starting function')
    time.sleep(0.1)
    print('Finished function')


if __name__ == '__main__':
    """
        p.terminate()
            == 0 > Success
             > 0 -> Had an error
             < 0 -> it was killed - interrupted with a signal code -15
    """
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())
    p.start()
    print('Process running:', p, p.is_alive())
    p.terminate()
    print('Process terminated:', p, p.is_alive())
    p.join()
    print('Process joined:', p, p.is_alive())
    print('Process exit code:', p.exitcode)

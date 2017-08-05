import threading


def function(i):
    print("function called by thread %i\n" %i)

threads = []
for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()
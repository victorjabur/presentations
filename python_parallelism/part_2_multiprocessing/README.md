# Diving into Python's Multiprocessing Module

## Thread based Parallelism
- Share the **memory** and **state** of the parent
- Are **light weight**
- Do not use Inter-Process Communication or messaging
- Python threads are **Posix Threads - pthreads**, real OS/Kernel level
- Python only allows a **single thread** to be executing within the interpreter **at once**. This restriction is enforced by the **GIL**
- **GIL (Global Interpreter Locker)** - this is a lock which must be acquired for a thread to enter the interpreter's space.
- **Only one** thread may be executing within the Python interpreter at once.
- GIL is not a bug. It is an implementation detail of **CPython** interpreter because it makes the maintenance easier.
- **I/O, sockets and http** communications don't suffer to much because the GIL.


## Process based Parallelism
- To solve **large problems** in a relatively **short time**
- Share nothing or little is **safer** than share everything
- They are **heavy weight** (in comparison to threads)
- Processes are "**share nothing**" - programmers must explicitly share any data/state - this means that the programmers are forced to **think** about what is being shared
- **Easier** to turn into a **distributed** application
- Most part of the time, they are **faster than threads** in Python, **because the GIL** problem

![](/home/jabur/app/github/presentations/python_parallelism/part_2_multiprocessing/images/process_threads.png)

## Multiprocessing Module

- Part of the **standard library** of the language added in Python 2.6
	- **import multiprocessing**
- **Originally** known as **pyprocessing** (a third-party extension module)
- This is a module for writing concurrent Python programs based on communicating processes
- A module that is **especially useful** for concurrent **CPU-bound** processing
- Using this module, there are **no shared data structures**, every process is completely **isolated**, so forget about all of that locking business
- **Everything** is focused on **messaging**
- Implements the **shared memory** programming paradigm
	- Multiple processors acessing a common memory
- Parent process **spawn a child process** and can continue its execution normally (assynchronously)
- It implements the **same API that threading module**, but it uses processes
- It offers **distributed-computing** facilities as well
- It **allows** data/memory sharing
- It is a great **alternative** to step aside the **GIL** problem

![](/home/jabur/app/github/presentations/python_parallelism/part_2_multiprocessing/images/multiprocessing_scheme.png)

### Supported ways of Communication

- **Queues**
	- [https://docs.python.org/3.7/library/multiprocessing.html#multiprocessing.Queue](https://docs.python.org/3.7/library/multiprocessing.html#multiprocessing.Queue) 
	
	- A queue supports **multiple producers** and **multiple consumers**
	- It could be a normal **Queue** or a **JoinableQueue**
	- It is thread and process safe
	- The **multiprocessing Queue** is a **clone** of traditional **Queue.queue**
	
![](/home/jabur/app/github/presentations/python_parallelism/part_2_multiprocessing/images/queue.png) 
	
- **Pipes**
	- [https://docs.python.org/3.7/library/multiprocessing.html#multiprocessing.Pipe](https://docs.python.org/3.7/library/multiprocessing.html#multiprocessing.Pipe)
	
	- A pipe is basically a **block of memory** in the kernel, a buffer that is read/written by some processes. The advantage of using pipes is that it has **2 files descriptors associated** with it, and thus sharing data between 2 processes is **as simple as reading/writing to a file**.
	- The pipe could be used in a **Linux shell**, like this: **cat foobar | wc -l**
	- It returns a pair of connection objects connected by a pipe which by default is duplex (two-way)
	- **It can only have two endpoints** - One of them should be used for read while the another for write in order to avoid risk of corruption
	- **Faster** than queues
	- You can send and receive Python objects (they will be serialized using pickle) using the communication channel

**Pipes in a Linux Shell Command**
In the following picture, you can see pipes in action inside the Linux when you type a command like this: "tail -f access.log | cut -d'' -f1 | uniq"

![](/home/jabur/app/github/presentations/python_parallelism/part_2_multiprocessing/images/linux_pipe.png) 

## Reference Links

- Take a look at the Official Documentation here:
	- [https://docs.python.org/3.7/library/multiprocessing.html](https://docs.python.org/3.7/library/multiprocessing.html)
- David Beazley - An Introduction to Python Concurrency - USENIX - San Diego, 2009
	- [https://www.slideshare.net/dabeaz/an-introduction-to-python-concurrency](https://www.slideshare.net/dabeaz/an-introduction-to-python-concurrency)
- David Beazley - Python Concurrency From the Ground Up: LIVE! - PyCon US, 2015
	- [http://pyvideo.org/video/3432/python-concurrency-from-the-ground-up-live](http://pyvideo.org/video/3432/python-concurrency-from-the-ground-up-live)
- Jesse Noller - Getting started with Concurrency - PyWorks - Atlanta, 2008
	- [https://www.slideshare.net/pvergain/multiprocessing-with-python-presentation](https://www.slideshare.net/pvergain/multiprocessing-with-python-presentation)
- Bernd Klein - Python Course - Pipes in Python
	- [http://www.python-course.eu/pipes.php](http://www.python-course.eu/pipes.php)
- Book: Python Parallel Programming Cookbook
	- Master efficient parallel programming to build powerful applications using Python
	[https://www.packtpub.com/application-development/python-parallel-programming-cookbook](https://www.packtpub.com/application-development/python-parallel-programming-cookbook)

## Parts of this Presentation

Here are some topics that will be addressed in Part 3 of this presentation: 

- Threads and Native Lockings (Part 1)
	- [https://github.com/victorjabur/presentations/tree/master/python_parallelism/part_1](https://github.com/victorjabur/presentations/tree/master/python_parallelism/part_1)
- Processes and Multiprocessing Module (Part 2 this)
- Concurrent.futures module in Python 3.2 (Part 3)
- Asyncio module in Python 3.4 (Part 4)
- Async/await syntax for native coroutines in Python 3.5 (Part 5)

## Take a Time for Reflection
![](/home/jabur/app/github/presentations/python_parallelism/part_2_multiprocessing/images/cartoon_reflection.png) 

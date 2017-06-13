#Parallelism in Python

##Why parallelism?
To solve large problems in a relatively short time

## Four Types of Machine's Architecture

- Single instruction, single data (**SISD**)
	- Uniprocessor machine - Single processor and memory
	- CPU = Fetch -> Code -> Execute

- Single instruction, multiple data (**SIMD**)
	- Multi identical processor (each with its own local memory)
	- All processors are controlled by a single instruction stream
	- Processors execute the same instruction, but on different data
	- Data level parallelism
	- GPU Processing - a lot of SIMD embedded units
	- Connection Machine (1985 Thinking Machine)
	- MPP (NASA 1983)

- Multiple instruction, single data (**MISD**)
    - Multiprocessor (each with their own control unit) - Single memory
    - Instruction level parallelism
    - Resolves a few real world problems
    - Theoretical computer

- Multiple instruction, multiple data (**MIMD**)
	- Multi processors and Multi data streams
	- Each processor has its own control unit and local memory
	- More computationally powerful
	- Each processor
	- Each processor has its own flow of instructions and control unit
	- Different programs on different data
	- Parallelism level with threads and/or processes
	- Processor usually operates asynchronously
	- It is difficult to design/implement/analyze asynchronous algorithms

## Commom Problems
- Memory could be lack (slow) for the processor (Cycle time)
- IRQ -> Interruption to handle the request of 1 processor at time
- Shared Memory x Distributed Memory (drawback)

## Shared Memory
- Bus Structure
- Each processor cache x synchronization x Other processors
- Hardware implementation to handle parallelism (like threads)
- One processor per time
- Different paradigms
	- UMA: Uniform time -> Difficult for programmers manage locks
	- NUMA: Non Uniform -> High speed in a Distributed memory with slower time for the processors
	- NORMA: No remote access -> Local memory for each processor and sync them
	- COMA: Cache only -> Mix between NUMA and NORMA -> remove duplicates


## Parallel Programming Models
Exists as an abstraction of hardware and memory architectures.

- Models:
	- **The shared memory model**
		- Programmer needs to control with locks, semaphores
		- Programmer don't worry with share data between the tasks
		- Performance drawback -> manage data locality (data same processor)
		- Multiple processors working in the same data -> Spent memory, cache, bus traffic
	- **The multithread model**
		- Process has multiple flows of execution
		- Is used on a shared memory system
		- Intel Hyper-threading implements multithreading on hardware -> 2 threads waiting for I/O
		- Programmer should manage synchronization between threads
		- Programmer should prevent data updates at the same location at the same time
		- Posix threads are a classical usage	
		- The distributed memory/message passing model
			- Known as MPI (message passing interface) model
			- Distributed memory (Network communication)
		- The data parallel model
			- Many tasks working in different portion of data
			- Programmer should care with the data partitioning / alignment

## How to design a parallel program?
- Challenge: Parallel without partial or erroneous results.
- Steps needed (Workflow):
	- **Task decomposition**
		- Split the program into tasks or a set of instructions -> execute on different processors
			- Domain Decomposition:
				- Same application, different portion of data, huge data
			- Functional Decomposition:
				- Different application, same data, huge data
	- **Task assignment**
		- Distribute the tasks among the processors (load balancing)
	- **Agglomeration**
		- Combining smaller tasks with large ones to improve performance (limited processor cores)
	- **Mapping**
		- Where each task will be executed to reduce communication between threads and reduce the total execution time
		- It is a NP-complete problem -> No polynomial time solutions to the problem in the general case
		- Dynamic Mapping: Load balance algorithms
			- Manage/worker -> Workers communicate with a Centralized Manager (distributed)
			- Hierarchical -> The same as above but Semi distributed -> groups of workers with sub-managers
			- Decentralize -> Each processor maintains its own task pool and communicates directly to other processors

## How to evaluate the performance?
- Limitations of a parallel computation: Ahmdal's law
- Degree of efficiency of parallelization of a sequential algorithm: Gustafson's law
	- Key performance indexes:
		- Speedup - Time taken by parallel way to solve a problem in comparison with the sequential one.
		- Efficiency - How well the processors are utilized / how much wasted time with communication/synchronization
		- Scaling - The ability to maintain the efficiency when more data and more processors are added 

## What is the difference between a Process and a Thread?
- Analogically, process is a new browser instance and a thread is each new tab.
	- **Process**
		- Consist of multiple parallel threads and it don't share data or resources.
		- Can spawn a hundred of threads and they will share space addressing and data structures.		
	- **Threads**
		- Multiple threads can share data and resources, taking advantage of the so-called space of shared information
		- A thread is a lightweight process and can be less onerous than that a real process in terms of CPU's resources.
		- The states of execution of a thread are generally called ready, running, and blocked
		- Advantage: Better performance as the context switch between threads is lighter for the O.S.
		- Multithreaded programming prefers a communication method between threads using the space of shared information

>Exercise
>> At this point you should view: Exercises 1, 2 and 3

## How Thread works in Python?
- Python manages a thread via the threading package that is provided by the Python standard library
- The major components of the threading module are:
	- The **thread** object
	- The **Lock** object
	- The **RLock** object
	- The **Semaphore** object 
		- Invented by E. Dijkstra
		- Used for the first time in an operational system
		- Abstract data type managed by the operational system
		- Used to synchronize the access by multiple threads to shared resources and data
		- It contains an internal variable that identifies the number of concurrent access to a resource to which it is associated
		- Based on the two functions acquire() and release()
		- Semaphore.release() increases the counter and semaphore.acquire() decrements it
	- The **Condtion** object
		- Is based on RLock
	- The **Event** object
		- An event object manages an internal flag that can be set to true with the set() method and reset to false with the clear() method.

###Summary about those methods
- **Lock** and **RLock** objects
	- It even works, but ... (only for learning purpose)
	- Subjected to harmful deadlock situations
	- Introduce unnecessary overhead
	- It limits the scalability
	- Possibility to impose the priority access to the shared memory by various processes
	- Difficult for debugging
	- Preferable to use another method in a real scenario

- **Semaphores**
	- Are still commonly used in programming languages that are multithreaded
	- It's a mutex (mutual exclusion in access to data and resources)
	- It works properly only if the wait and signal operations are performed in atomic blocks
	- The fact that the wait operation was not performed in atomic terms has led to a solution of the stall
	- Using them you can run into situations of deadlock

- **Condition**
	- The internal class _Condition creates a RLock() object if no existing lock is passed to the class's constructor.

~~~python
		class _Condition(_Verbose):
			def __init__(self, lock=None, verbose=None):
				_Verbose.__init__(self, verbose)
				if lock is None:
					lock = RLock()
				self.__lock = lock
~~~
- **Event**

- **With Statement**

-  **Queues**: A coarse-grained lock instead of a fine-grained locking model 

	- **Queue** Classes
	- class queue.Queue
	- class queue.LifoQueue
	- class queue.PriorityQueue -> sorted(list(entries))[0])

	- **Queue** functions
	- Queue.put(item, block=True, timeout=None)
	- Queue.get(block=True, timeout=None)
	- Queue.put_nowait(item)
	- Queue.get_nowait()
	- Queue.join()
	- Queue.qsize()
	- Queue.empty()
	- Queue.full()

> Full and awesome official documentation about Python Queues
> [https://docs.python.org/3/library/queue.html](https://docs.python.org/3/library/queue.html)

## The BIG problem: GIL (Global Interpreter Locker)

The Python language was designed to use a locker system called GIL that causes lots of problems when you try to run REAL parallel code in Python. In some cases even when you use threads your code isn't parralel because this *feature*.  Here is a good reference to read about this problem.

>[http://python-notes.curiousefficiency.org/en/latest/python3/multicore_python.html](http://python-notes.curiousefficiency.org/en/latest/python3/multicore_python.html) 

# Additional Content

David Beazley is an american celebrity when the subject is Python, here you can watch one of the best videos that I've ever seen about the Python language and their parallelism features.

> [http://pyvideo.org/video/3432/python-concurrency-from-the-ground-up-live](http://pyvideo.org/video/3432/python-concurrency-from-the-ground-up-live) 

# Some alternatives to skip GIL

- CPython and PyPy
- threading to be used for concurrent synchronous IO calls
- multiple processes can be used for concurrent CPU bound calculations
- Numba module / Cython
- https://github.com/google/grumpy (Compile to Go)
- Apache Spark
- http://pyparallel.org/

- It isn't a truly free-threaded interpreter ...
- any free threaded solution that retains the reference counting GC will still need a global threads in the CPython runtime will mean updating the reference counts on a whole new working set of objects, almost certainly blowing the CPU cache and losing some of the speed benefits gained from making more effective use of multiple cores

# Next Topics (part 2)

Here are some topics that will be addressed in Part 2 of this presentation: 

- Multiprocessing module
- Concurrent.futures module in Python 3.2
- Asyncio module in Python 3.4
- Async/await syntax for native coroutines in Python 3.5

>	Credits: Giancarlo Zaccone
	Publisher: Packt Publishing
	Book: Python Parallel Programming Cookbook
	Master efficient parallel programming to build powerful applications using Python
	https://www.packtpub.com/application-development/python-parallel-programming-cookbook

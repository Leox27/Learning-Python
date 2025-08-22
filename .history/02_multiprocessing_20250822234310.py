### Multiprocessing -

import multiprocessing
import time

def square_number():
    for i in range(7):
        time.sleep(2)
        print(f"Square: {i * i}")

def cube_number():
    for i in range(7):
        time.sleep(2)
        print(f"Cube: {i * i * i}")

if __name__ == "__main__":
    
    processes = []
    for i in range(7):
        # Create two processes for each function
        p1 = multiprocessing.Process(target=square_number)
        p2 = multiprocessing.Process(target=cube_number)

        # Pass the current number to both processes
        processes.append(p1)
        processes.append(p2)

        t = time.time()
        p1.start()
        p2.start()

        p1.join()
        p2.join()

        finished = time.time() - t
        print(f"Finished in {finished} seconds")

### OUTOUT:

# [Running] python -u "c:\workplace\Python practice\ch_14_threading_&_processing\02_multiprocessing.py"
# Square: 0
# Square: 1
# Square: 4
# Square: 9
# Square: 16
# Square: 25
# Square: 36
# Cube: 0
# Cube: 1
# Cube: 8
# Cube: 27
# Cube: 64
# Cube: 125
# Cube: 216
# Finished in 14.116031169891357 seconds

### Key Points -
# Multiprocessing means running multiple processes at the same time. 
# Each process has its own memory space and Python interpreter, so they don’t interfere with each other.

# In Python, this is especially useful because of the Global Interpreter Lock (GIL):

# 1. Threads can’t truly run Python code in parallel (they take turns).

# 2. But multiprocessing bypasses the GIL by using separate processes, allowing true parallelism on multiple CPU cores.

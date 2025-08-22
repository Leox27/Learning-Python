###

import threading
import time

def print_numbers():
    for i in range(7):
        time.sleep(2)
        print(f"Number: {i}\n")

def print_latter():
    for letter in 'abcdefg':
        time.sleep(2)
        print(f"Letter: {letter}\n")

t = time.time()
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_latter)

t1.start()
t2.start()

t1.join()
t2.join()

finished = time.time() - t

print(f"Finished in {finished} seconds")

# OUTPUT:
## [Running] python -u "c:\workplace\Python practice\ch_14_threading_&_processing\01_threading.py"
# Number: 0

# Letter: a

# Number: 1

# Letter: b

# Number: 2

# Letter: c

# Number: 3

# Letter: d

# Number: 4

# Letter: e

# Number: 5

# Letter: f

# Number: 6

# Letter: g

# Finished in 14.01324200630188 seconds

## [Done] exited with code=0 in 14.132 seconds

### Use -
# A thread is like a lightweight subprocess. 
# Multiple threads share the same memory space (unlike processes, 
# which each have separate memory). This makes threading useful 
# for tasks where programs need to do multiple things seemingly at the same time, such as:

# 1. Handling multiple user requests in a server

# 2. Downloading files while processing them

# 3. Running background tasks (like timers, schedulers, or monitoring)
import numpy as np
import queue 
import threading
import multiprocessing
import time

def matrix_multiplication(A,B):
    return np.matmul(A,B)

#threads
def thread_func(q):

    while True:
        try: 
            A, B = q.get(timeout = 1)
            result = matrix_multiplication(A,B)
            print(f"{result}")
        except queue.Empty:
            break

#test thread
def test_thread(num_threads, queue_size, matrow, matcol):

    print("Test: Threading")

    q = queue.Queue(maxsize = queue_size)
    
    for i in range(queue_size):
        A = np.random.rand(matrow, matcol)
        B = np.random.rand(matrow, matcol)
        #time.sleep(1)
        q.put((A,B))

    tracker = []

    for i in range(num_threads):
        thread = threading.Thread(target = thread_func, args = (q,))
        tracker.append(thread)
        thread.start()
    
    for i in tracker:
        i.join()

    print("Finished!")

def mp_func(q):

    while True:
        try: 
            A, B = q.get(timeout = 1)
            result = matrix_multiplication(A,B)
            print(f"{result}")
        except:
            break

#multiprocessor
def test_processor(num_processor, queue_size, matrow, matcol):
    print("Test: MultiProcessing")

    q = multiprocessing.Queue()

    for i in range(queue_size):
        A = np.random.rand(matrow, matcol)
        B = np.random.rand(matrow, matcol)
        #time.sleep(1)
        q.put((A,B))
    
    tracker = []

    for i in range(num_processor):
        processor = multiprocessing.Process(target = mp_func, args = (q,))
        tracker.append(processor)

        processor.start()
    
    for i in tracker:
        i.join()
    
    print("Finished")



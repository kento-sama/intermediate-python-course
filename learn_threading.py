from threading import Thread, Lock, current_thread
import time
from queue import Queue

database_value = 0 # db simulation

def increase(lock):
    global database_value
    
    # lock.acquire() # prevents other thread from proceeding
    # local_copy = database_value
    
    # local_copy += 1
    # time.sleep(0.1)
    # database_value = local_copy
    # lock.release() # allows other thread to proceed
    
    with lock: # automatic acquire and release
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
        

def worker(q, lock):
    while True:
        value = q.get()
        
        with lock:
            print(f"in {current_thread().name} got {value}")
            q.task_done()
        
if __name__ == '__main__':
    print("start value", database_value)
    
    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("end value", database_value)
    print("end main")
    
    q = Queue()
    
    num_threads = 10
    
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True
        thread.start()
        
    for i in range(1, 21):
        q.put(i)
        
    q.join()
        
    print("end main")
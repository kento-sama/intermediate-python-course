from multiprocessing import Process, Value, Array
import os
import time

def square_numbers():
    for i in range(1000):
        i * i
        time.sleep(0.1)
        
def add_100(num):
    for i in range(100):
        time.sleep(0.01)
        num.value += 1

if __name__ == '__main__':
    # processes = []
    # number_of_processes = os.cpu_count()

    # for i in range(number_of_processes):
    #     p = Process(target=square_numbers)
    #     processes.append(p)

    # for p in processes:
    #     p.start()

    # for p in processes:
    #     p.join()

    # print("end main")
    
    shared_number = Value('i', 0)
    print('Number at beginning is', shared_number.value)
    
    p1 = Process(target=add_100, args=(shared_number,))
    p2 = Process(target=add_100, args=(shared_number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Number at end is", shared_number.value)
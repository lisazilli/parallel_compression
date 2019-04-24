import datetime
import multiprocessing
import os
import shutil
import subprocess
import sys
import time
from multiprocessing import Lock, Process, Queue, current_process
from Queue import Empty

prnt_lock = multiprocessing.Lock()

def extract(ssys_to_extr, otpt_fldr_locn):
    while True:
        try:
            ssys = ssys_to_extr.get_nowait()
        except Empty:
            break
        else:
            prnt_lock.acquire()
            try:
                print("Extracting " + ssys + " with " + current_process().name)
            finally:
                prnt_lock.release()
            
            cmd = ['7z', 'x', otpt_fldr_locn + '\\' + ssys, '-aoa', '-y', '-oL:\\']
            p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            p.wait()

            # Print finished action to command line
            prnt_lock.acquire()
            try:
                print(current_process().name + " is done extracting " + ssys)
            finally:
                prnt_lock.release()

    return True
    
def main():   
    max_nbr_of_prcs = multiprocessing.cpu_count()
    ssys_to_extr = Queue()
    prcs= []

    # Ensure we have all arguments
    if (len(sys.argv) < 3 ):
        print("Need the following inputs:\n")
        print("1. Location of zip files\n")
        print("2. Number of processors to use\n")
        sys.exit()

    # Output location
    otpt_fldr_locn = sys.argv[-2]

    # Ensure the number of processes is actually a number
    try:
        nbr_of_prcs = int(sys.argv[-1])
    except:
        print("Need the number of processors as an integer.\n")
        sys.exit()

    # Ensure number of processes requested doesn't exceed the max
    if nbr_of_prcs > max_nbr_of_prcs:
        nbr_of_prcs = max_nbr_of_prcs
        print("Max number of processors available is " + str(max_nbr_of_prcs) +
              ". Default to " + str(max_nbr_of_prcs) + " processors.")

    # Add subsystems to queue
    ssys = os.listdir(otpt_fldr_locn)
    for item in ssys:
        ssys_to_extr.put(item)  
        
    # creating processes
    for w in range(nbr_of_prcs):
        p = Process(target=extract, args=(ssys_to_extr, otpt_fldr_locn))
        prcs.append(p)
        p.start()

    # completing process
    for p in prcs:
        p.join()
        
    return True

if __name__ == '__main__':
    main()
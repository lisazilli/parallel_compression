import datetime
import multiprocessing
import os
import random
import shutil
import subprocess
import sys
import time
from multiprocessing import Lock, Process, Queue, current_process
from Queue import Empty

prnt_lock = multiprocessing.Lock()

def compress(fldr_to_cmps, otpt_fldr_locn):
    while True:
        try:
            fldr = fldr_to_cmps.get_nowait()
        except Empty:
            break
        else:
            # Get the name of the file to compress
            fldr_path = fldr.split("\\")
            file_name = fldr_path[-1]

            # Print action to command line
            prnt_lock.acquire()
            try:
                print("Zipping " + file_name + " with " + current_process().name)
            finally:
                prnt_lock.release()

            # Perform compression
            cmd = ['7z', 'a', '-y', '-mmt', '-mx3', '-spf2', otpt_fldr_locn + '\\' + file_name + '.7z', fldr]
            p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            p.wait()

            # Print finished action to command line
            prnt_lock.acquire()
            try:
                print(current_process().name + " is done zipping " + file_name)
            finally:
                prnt_lock.release()
            
    return True
    
def main():   
    max_nbr_of_prcs = multiprocessing.cpu_count()
    fldr_to_cmps = Queue()
    prcs = []

    # Ensure we have all arguments
    if (len(sys.argv) < 3 ):
        print("Need the following inputs:\n")
        print("1. List of folder locations to compress\n")
        print("2. Output location\n")
        print("3. Number of processors to use\n")
        sys.exit()

    # Folders to compress
    for fldr in sys.argv[1:len(sys.argv) - 2]:
        fldr_to_cmps.put(fldr)

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

    # Creating processes
    for w in range(nbr_of_prcs):
        p = Process(target=compress, args=(fldr_to_cmps, otpt_fldr_locn))
        prcs.append(p)
        p.start()

    # Completing process
    for p in prcs:
        p.join()
           
    return True

if __name__ == '__main__':
    main()
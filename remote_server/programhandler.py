import signal 
import resource 
import os 
import sys

import subprocess

# checking time limit exceed 

# max run time of 15 millisecond 
if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Usage: programhandler.py <cpu time in seconds> <path to file to be run>")
    else:
        
        print(subprocess.run(["python", sys.argv[2]], capture_output=True, timeout=float(sys.argv[1])))
        print("Finished without running out of time or memory")


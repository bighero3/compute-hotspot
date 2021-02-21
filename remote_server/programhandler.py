import sys
import os
import subprocess

# checking time limit exceed 

# max run time of 15 millisecond 
if __name__ == '__main__':
    if len(sys.argv)!=3:
        print("Usage: programhandler.py <cpu time in seconds> <path to file to be run>")
    else:

        j=0
        for i in range(len(sys.argv[2])):
            if sys.argv[2][i] == "/":
                j=i
        newdir = sys.argv[2][:j]
        print(os.getcwd() +"/"+ newdir)
        print(subprocess.run(["python3.8", sys.argv[2][j+1:]], capture_output=False, timeout=float(sys.argv[1]), cwd=os.getcwd() +"/"+ newdir))
        print("Finished without running out of time or memory")


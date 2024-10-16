#import logging_config
import sys
from zoautil_py import datasets 


# total arguments
n = len(sys.argv)
print("Total arguments passed: ", n)

def printname(dsn):
    print("Testing python and IZOAU")
    print("Dataset " + dsn + " exists: " + str(datasets.exists(dsn)))

if (n > 2):
    print("Pass 1 parameter (dataset name) or less (use default dataset name)") 
elif (n==1):
    printname("Default name: YOURDSN.A.CNTL")
else:
    printname(sys.argv[2])
    

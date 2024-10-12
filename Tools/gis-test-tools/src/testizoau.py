#import logging_config
import sys
from zoautil_py import datasets 

# Create dataset so that we can force error
#datasets.create("ZOAU.DATASET", type="PDS", length=133, format="FBA", size="5M", verbose=True, debug=True)
# Force error
#datasets.create("ZOAU.DATASET", type="PDS", length=133, format="FBA", size="5M", verbose=True, debug=True)

# total arguments
n = len(sys.argv)
print("Total arguments passed: ", n)

def printname(dsn):
    print("Testing python and IZOAU")
    print("Dataset " + dsn + " exists: " + str(datasets.exists(dsn)))

if (n > 2):
    print("Pass 1 parameter (dataset name) or less (use default dataset name)") 
elif (n==1):
    printname("YOUTDSNx`x`.A.CNTL")
else:
    printname(sys.argv[1])
    

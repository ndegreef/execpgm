# Introduction 
Gathering some general tools here.

# Getting Started
The tools are distributed automatically to the XAT system.
Currently the go to
/u/greefn/zos-testtools

# Build and Test
The pipeline triggered by a push builds, deploys to XAT and performas some tests

# Environment settings
You need to make sure your Unix environment is properly set up.
Make sure the .profile file in your home directory contains the correct setting.
A sample .profile is added in /src, names `.profile (sample)`

# Contribute
Anyone with access to this repository is invited to add to the tools and enhance them. 

# Tools
All source code for the tools is in the /src folder.

## testizoau.py
Performs a minimal test with python and IBM Z Open Automation utilities.

Execute with command:
```
python3 testizoau.py
```
Expected output:
```
/u/greefdn/gis-testtools/dev:>python3 testizoau.py GREEFDN.A.DATA 
Total arguments passed:  2                                        
Testing python and IZOAU                                          
Dataset GREEFDN.A.DATA exists: False                              
```
## testmq.py - testing the MQ REST API's
A sample program to illustrate how you can interact with the MQ API's.

The shell script testmqpy.sh shows how to invoke this python program.

## testzws.py - testing the ZWS / IWS REST API's
A sample program to illustrate how you can interact with the ZWS API's.
Needs furhter documentation.

## testzosmffileapi.py
Program to test the z/OSMF file API's.
Work in progress...



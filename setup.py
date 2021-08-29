#!/usr/bin/python3
import sys
import os
import subprocess

'''
This should be run first to sent up the directory structure and moved the configs.
'''

def makeOpsStructure(opsfolder='/aaa/'):
    mkdirsCmd = ['mkdir', '-p', opsfolder+'mine/logs', opsfolder+'etc', opsfolder+'bin', opsfolder+'loot', '/data']
    subprocess.run(mkdirsCmd)

if __name__ == "__main__":
    if not os.getuid() == 0:
        print("You must be root!")
        sys.exit(0)
    
    makeOpsStructure()

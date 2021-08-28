#!/usr/bin/python3
import sys
import os
import subprocess


if __name__ == "__main__":
    if not os.getuid() == 0:
        print("You must be root!")
        sys.exit(0)
    
    mkdirsCmd = ['mkdir', '-p', '/aaa/mine/logs', '/aaa/etc', '/aaa/bin', '/aaa/loot']
    subprocess.run(mkdirsCmd)
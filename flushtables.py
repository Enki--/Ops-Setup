#!/usr/bin/python3
import sys
import os
import subprocess
import fwrules

if __name__ == "__main__":
    # This is all just for testing
    # iptables requires root, so we check, and exit if not
    if not os.getuid() == 0:
        print("You must be root!")
        sys.exit(0)
    test = fwrules.IpTable()
    test.returnTablesDefault()
    test.flushTables()
    #test.addOutputRule(destination="1.1.1.1/24")
    #test.addInputRule(source="2.2.2.2")
    
    print(test)




# to watch hits in real time
# sudo watch -d iptables -v -L
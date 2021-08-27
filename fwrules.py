#!/usr/bin/python3
import sys
import os
import subprocess

class IpTable:
    def __init__(self):
        # Bring chains to a good state, then default DROP everything, then allow loopback
        self.flushTables()
        self.returnTablesDefault()
        # drop all INPUT
        defaultDropInputCmd = ['/usr/sbin/iptables', '-P', 'INPUT', 'DROP']
        # drop all OUPUT
        defaultDropOutputCmd = ['/usr/sbin/iptables', '-P', 'OUTPUT', 'DROP']
        # drop all FORWARD
        defaultDropForwardCmd = ['/usr/sbin/iptables', '-P', 'FORWARD', 'DROP']      
        # Allow Loopback
        loopbackInCmd = ['/usr/sbin/iptables', '-A', 'INPUT', '-i', 'lo', '-j', 'ACCEPT' ]       
        loopbackOutCmd = ['/usr/sbin/iptables', '-A', 'OUTPUT', '-o', 'lo', '-j', 'ACCEPT' ]
        # Run them All
        subprocess.run(defaultDropInputCmd)
        subprocess.run(defaultDropOutputCmd)
        subprocess.run(defaultDropForwardCmd) 
        subprocess.run(loopbackInCmd)
        subprocess.run(loopbackOutCmd)

    def __str__(self) -> str:
        # prints the current iptables chains
        output = subprocess.check_output(['iptables', '-L'])
        # returns as utf-8, so we need to decode
        output = output.decode("utf-8")
        # Return asscii for printing
        return(output)

    def flushTables(self):
        #Flushes all chains
        flushInputCmd = ['/usr/sbin/iptables', '--flush', 'INPUT']
        flushOutputCmd = ['/usr/sbin/iptables', '--flush', 'OUTPUT']
        flushForwardCmd = ['/usr/sbin/iptables', '--flush', 'FORWARD']
        subprocess.run(flushForwardCmd)
        subprocess.run(flushInputCmd)
        subprocess.run(flushOutputCmd)

    def returnTablesDefault(self):
        #chains are accept by default, so setting them to ACCEPT
        defaultDropInputCmd = ['/usr/sbin/iptables', '-P', 'INPUT', 'ACCEPT']
        defaultDropOutputCmd = ['/usr/sbin/iptables', '-P', 'OUTPUT', 'ACCEPT']
        defaultDropForwardCmd = ['/usr/sbin/iptables', '-P', 'FORWARD', 'ACCEPT']
        subprocess.run(defaultDropForwardCmd)   
        subprocess.run(defaultDropOutputCmd)
        subprocess.run(defaultDropInputCmd)

    def addOutputRule(self, proto="tcp", port='80', interface='eth0', destination="0.0.0.0/0"):
        #create and add OUTPUT chain rule
        addOutputRuleCmd = ['/usr/sbin/iptables', '-A', 'OUTPUT', '-p', proto, '--dport', port, '-d', destination, '-o', interface, '-j', 'ACCEPT']
        subprocess.run(addOutputRuleCmd)

    def addInputRule(self, proto="tcp", port='80', interface='eth0', source="0.0.0.0/0"):
        #create and add INPUT chain rule
        addInputRuleCmd = ['/usr/sbin/iptables', '-A', 'INPUT', '-i', interface, '-p', proto, '--sport', port, '-s', source, '-j', 'ACCEPT']
        subprocess.run(addInputRuleCmd)

if __name__ == "__main__":
    # iptables requires root, so we check, and exit if not
    if not os.getuid() == 0:
        print("You must be root!")
        sys.exit(0)
    table = IpTable()
    print(table)




# to watch hits in real time
# sudo watch -d iptables -v -L
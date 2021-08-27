#!/usr/bin/python3
import sys
import os
import subprocess

class TerminalSetup:
    def __init__(self):
        if not os.getuid() == 0:
            print("You must be root!")
        
    def NewTgtTerm(self, terminatorConfig = 'etc/terminator', geometry='1000x400-0+0'):
        newTgtCmd = ['terminator', '-g', terminatorConfig, '-p', 'tgt', '--geometry='+geometry]
        subprocess.Popen(newTgtCmd, start_new_session=True)
    
    def NewLocalTerm(self, terminatorConfig = 'etc/terminator', geometry='1000x400-50+50'):
        newTgtCmd = ['terminator', '-g', terminatorConfig, '-p', 'local', '--geometry='+geometry]
        print(newTgtCmd)
        subprocess.Popen(newTgtCmd, start_new_session=True)    

    def TgtTermExeCmd(self, command, terminatorConfig = 'etc/terminator', geometry='1000x400-0+0'):
        newTgtCmd = ['terminator', '-g', terminatorConfig, '-p', 'tgt', '--geometry='+geometry, '-e', command]
        print(newTgtCmd)
        subprocess.Popen(newTgtCmd, start_new_session=True)
    
    def LocalTermExeCmd(self, command, terminatorConfig = 'etc/terminator', geometry='1000x400-50+50'):
        newTgtCmd = ['terminator', '-g', terminatorConfig, '-p', 'local', '--geometry='+geometry, '-e', command]
        print(newTgtCmd)
        subprocess.Popen(newTgtCmd, start_new_session=True)    

if __name__ == "__main__":
    test = TerminalSetup()
    test.NewTgtTerm()
    test.NewLocalTerm()
    test.LocalTermExeCmd('watch -n1 -d ip -s link show eth0')
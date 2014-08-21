#! /usr/bin/python3

#Script to install vmware on the computer must have the vmware-tools-distrib
# folder already copied into the vmware folder.  I may be able to do something 
# with that later to automate it. 

import os

def main():

#    os.system("cd /home/jonl316/vmware/vmware-tools-distrib")
    os.chdir("/home/jonl316/vmware/")
    os.system("tar -xvf /home/jonl316/vmware/VMwareTools*")
    os.chdir("/home/jonl316/vmware/vmware-tools-distrib")
    os.system("sudo ./vmware-install.pl -d")


if __name__ == "__main__":
    main()

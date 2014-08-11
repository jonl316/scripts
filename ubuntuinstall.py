#! /usr/bin/python3

#Python script to update ubuntu and setup git and install other programs

import os

def main():

    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade -y")
    os.system("sudo apt-get install git -y")
    print("git has been installed")
    os.system("sudo apt-get install terminator -y")
    os.system("sudo apt-get install vim -y")
    os.system("sudo apt-get install filezilla -y")
    os.system("sudo apt-get install chromium-browser -y")
    os.system("sudo apt-get install guake -y")
    
     
    os.system("git config --global user.name \"Jonathan David Livesay\"")
    os.system("git config --global user.email \"jonathan.livesay@gmail.com\"")
    os.system("git config --global color.ui true")

    print("Install Complete!!")    

if __name__ == "__main__":
    main()

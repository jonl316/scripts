#!/usr/bin/python3 -tt
# Python app to automate creating folders in Linux 
# this is a test though 
# Eventually this will create an ~/opt/ folder in the home dir
# and create other folders in there that I usually move over
# all the time.

import sys
import os 

def createDirectory(path):
  if not os.path.exists(path):
      os.makedirs(path)
      print(path + ': Created!')
  else: 
      print(path + ': already exists')

def main():

# Set the default working directory to /home/jonl316 because that is how I mostly 
# set up new computers with that username and I want create these folders there. 
    strWorkingPath = '/home/jonl316/'
    choice = ''
    
    # Logic for picking another path is /home/jonl316 doesn't work.  
    print('Default working path has been set to: ' + strWorkingPath)
    choice = input('Would you like to use the default path? (Y or N): ')
    choice = choice[0].upper()
    
    # if statement so that I can type in another path to create these folders in 
    # if I don't want them to go into the /home/jonl316 folder
    if choice != 'Y':
        strWorkingPath = input('Please enter the beginning working path: ')
        
    while(os.path.exists(strWorkingPath) != True):
        strWorkingPath = input('Please enter the beginning path:  ')

    if os.path.exists(strWorkingPath):
        print('path is good!!')
        os.chdir(strWorkingPath)


    createDirectory('opt/EclipseJava/workspace')
    createDirectory('opt/EclipsePerl/workspace')
    createDirectory('opt/EclipsePython/workspace')
    createDirectory('opt/EclipseCPP/workspace')
    createDirectory('opt/EclipseJavaEE/workspace')
    createDirectory('opt/CodeBlocksProjects')
    createDirectory('opt/NetBeansProjects')
    createDirectory('opt/NetBeans')
    createDirectory('opt/IdeaProjects')
    createDirectory('opt/PythonProjects')
    createDirectory('vmware')
    createDirectory('opt/Idea')
    createDirectory('opt/AA')
    createDirectory('opt/SpringSTS/workspace')
    createDirectory('opt/PyCharm')
    createDirectory('opt/PyCharmProjects')


    print('\n****** End Program ******')

if __name__ == "__main__":
    main()

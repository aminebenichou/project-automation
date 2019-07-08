import os
import subprocess

projName = input('Enter project name : ')
path = os.getcwd() + '\\' + projName
navdir = 'cd ' + projName
dj= 'django-admin startproject ' + projName
try:
    # Create target Directory
    os.mkdir(projName)
        
    print("Directory " , projName ,  " Created ") 
except FileExistsError:
    print("Directory " , projName ,  " already exists")
try:
    #getting into the created directory
    os.chdir(path)
    print(os.getcwd())
except:
    print("error")
try:
    #create a read me file
    open('readMe.txt', 'a').close()
    print("readme file created successfully")
except:
    print("error ceating readme file")
#running vscode
subprocess.call('code .', shell=True)
print('Launching vs Code...')
try:
    #creating django project
    subprocess.call(dj, shell=True)
    print('Creating django project')
except:
    print('Cannot create django project')

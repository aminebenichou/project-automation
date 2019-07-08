import os
import subprocess

projName = input('Enter project name : ')
path = os.getcwd() + '\\' + projName
fc= 'flutter create ' + projName
try:
    # Create target Directory
    os.mkdir(projName)
    
    
    print("Directory " , projName ,  " Created ") 
except FileExistsError:
    print("Directory " , projName ,  " already exists")
try:

    os.chdir(path)
    print(os.getcwd())
except:
    print("error")
try:

    open('readMe.txt', 'a').close()
    print("readme file created successfully")
except:
    print("error ceating readme file")
#running vscode
subprocess.call('code .', shell=True)
print('Launching vs Code...')
subprocess.call(fc, shell=True)
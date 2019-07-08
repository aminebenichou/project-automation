import os
import subprocess

projName = input('Enter project name : ')
path = os.getcwd() + '\\' + projName
try:
    # Create target Directory
    os.mkdir(projName)
    
    print("Directory " , projName ,  " Created ") 
except FileExistsError:
    print("Directory " , projName ,  " already exists")
try:
    #get into the created directory
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
try:
    #running vscode
    subprocess.call('code .', shell=True)
    print('Launching vs Code...')
except:
    print('ERROR launching vs Code...')
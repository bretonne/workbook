# Exercise 141: Display the Head of a File
# (Solved—40 Lines)
# Unix-based operating systems usually include a tool named head. It displays the
# first 10 lines of a file whose name is provided as a command line parameter. Write
# a Python program that provides the same behavior. Display an appropriate error
# message if the file requested by the user does not exist or if the command line
# parameter is omitted.

import os.path

#filePath = "C:/aa/Git/IPS_LKA2.0-Infrastructure-Release/Infrastructure/LookAhead/Gigaspaces/Scripts/DEV/ATC/gsstop.sh"
filePath = r"C:\aa\Git\IPS_LKA2.0-Infrastructure-Release\Infrastructure\LookAhead\Gigaspaces\Scripts\DEV\ATC\gsstop.sh"
my_path = os.path.abspath(os.path.dirname(__file__))
print("my path is ", my_path)

f = open(filePath, "r")
line = f.readline()
index=0
while line!="" and index<10:
    print(line)
    line = f.readline()
    index +=1
f.close()


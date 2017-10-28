import os
HOME_DIR = '/Users/jmartin'
testPath = os.path.join('usr', 'bin')
print(testPath)

# Get current working directory
cwd = os.getcwd() + '/Misc/AutomateTheBoringStuffWithPython'
print(cwd)

FILE_LOC = f"{cwd}/ch_8__files.py"
# Make directories

dname = os.path.dirname(FILE_LOC)
bname = os.path.basename(FILE_LOC)
print(dname, bname, os.path.split(FILE_LOC))

sizeOfFile = os.path.getsize(FILE_LOC)
print(f"size of file: {sizeOfFile} bytes")

fileListInDirectory = os.listdir(os.getcwd())
print(f"fileListInDirecotry: {fileListInDirectory}")



helloFile = open(f"{HOME_DIR}/hello.txt")
print(helloFile.readlines())
# print(helloFile.read())
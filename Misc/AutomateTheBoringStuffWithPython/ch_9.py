import os
import pprint

for folderName, subfolders, filenames in os.walk('/'):
    print("Cur folder is:" + folderName)

    data = {
        'subfolders': [],
        'filenames': []
    }

    for subfolder in subfolders:
        # print(f"subfolder of: {folderName}: {subfolder}")
        data['subfolders'] += [subfolder]

    for filename in filenames:
        # print(f"FILE INSIDE: {folderName} : {filename}")
        data['filenames'] += [filename]

    pprint.pprint(data)
    print("-------------------------------------------------------------")
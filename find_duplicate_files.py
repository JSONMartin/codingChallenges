"""
Source: https://www.interviewcake.com/question/javascript/find-duplicate-files

You left your computer unlocked and your friend decided to troll you by copying a lot of your files to random spots all over your file system.

Even worse, she saved the duplicate files with random, embarrassing names ("this_is_like_a_digital_wedgie.txt" was clever, I'll give her that).

Write a function that returns an array of all the duplicate files. We'll check them by hand before actually deleting them,
since programmatically deleting files is really scary. To help us confirm that two files are actually duplicates, return an array of arrays where:
- the first item is the duplicate file
- the second item is the original file

For example:

  [ ['/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'],
  ['/home/trololol.mov', '/etc/apache2/httpd.conf'] ]

You can assume each file was only duplicated once.
"""

import os
import hashlib

def find_duplicate_files(path):
    file_md5_dictionary = {}

    for root, dirs, files in os.walk(path): # Walk through each file and subdirectory, starting in the root
        for name in files:
            path = os.path.join(root, name)
            print "Currently processing file:" + path
            file_hash = hash_file(path)
            file_info = (path, os.path.getctime(path))
            if file_hash in file_md5_dictionary:
                file_md5_dictionary[file_hash].append(file_info)
            else:
                file_md5_dictionary[file_hash] = [file_info]

    def sort_duplicate_files(duplicate_file_dictionary):
        duplicate_list = []
        for hash in duplicate_file_dictionary:
            sorted_list = sorted(duplicate_file_dictionary[hash], key=lambda x: x[1], reverse=True) # key=lambda x: x[1] makes the sorted function sort on the 2nd value of the tuple, reverse=True sorts from newest to oldest

            if len(sorted_list) >= 2:
                duplicate_file_array = []
                print "Duplicate found for [%s]:" % hash, sorted_list
                for file in sorted_list:
                    duplicate_file_array.append(file[0])
                duplicate_list.append(duplicate_file_array)

        return duplicate_list

    return sort_duplicate_files(file_md5_dictionary)

def hash_file(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()

def sample_hash_file(path): # This is an optimized version of the hashfile method I wrote above, where it samples 3 spots in the beginning, middle, and end, rather than hashing the entire contents of the file. Changes the time complexity from O(N) to O(1).

    num_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(path)

    hasher = hashlib.sha512()

    with open(path, 'rb') as file:

        # if the file is too short to take 3 samples, hash the entire file
        if total_bytes < num_bytes_to_read_per_sample * 3:
            hasher.update(file.read())

        else:
            num_bytes_between_samples = (total_bytes - num_bytes_to_read_per_sample * 3) / 2

            # read first, middle, and last bytes
            for offset_multiplier in xrange(3):
                start_of_sample = offset_multiplier * (num_bytes_to_read_per_sample + num_bytes_between_samples)
                file.seek(start_of_sample)
                sample = file.read(num_bytes_to_read_per_sample)
                hasher.update(sample)

    return hasher.hexdigest()

"""
TEST CASES
"""
#print find_duplicate_files('/Users/jsonmartin/filetest')
#print find_duplicate_files('/Users/jsonmartin/filetest2')

dups = find_duplicate_files('/Users/jsonmartin/Dropbox/code/htdocs') # Finishes in 9.8 sec with sample_hash_file implementation, 12.53 with hash_file implementation
for duplicate in dups:
    print duplicate
import os
import sys
import hashlib

BUF_SIZE = 65536  

def count_files(path):
  count = 0

  for root, subdirs, files in os.walk(path):
    for filename in files:
      count = count + 1

  return count

def remove_duplicates(path):
  unique_files = set()
  remove_list = []
    
  print ('Hashing...')
  for root, subdirs, files in os.walk(path):
    for filename in files:
       full_path = os.path.join(root, filename)
       file_hash = hash_file(full_path, BUF_SIZE)
       if file_hash in unique_files:
          remove_list.append(full_path)
       else:
          unique_files.add(file_hash)

  print ("Removing...")
  num_removals = len(remove_list)
  for file in remove_list:
     os.remove(file)

  return num_removals

def hash_file(file_name, buffer_size):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()

    with open(file_name, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            sha1.update(data)

    return sha1.hexdigest()

num_args = len(sys.argv)
if num_args < 2:
  print ("USAGE: duplicateremover [source folder]")
  sys.exit()

num_removed = remove_duplicates(sys.argv[1])
print (num_removed)




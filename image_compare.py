import cv2
import sys
import os
import numpy as np


def compare_images(source_dir, threshold):
    # First construct a list of all files in the source folder
    file_list = []
    files_to_remove = []
    for root, subdirs, files in os.walk(source_dir):
        for filename in files:
            full_path = os.path.join(root, filename)
            file_list.append(full_path)
            
    # compare every file to every other and output hash difference
    i = 0
    for start_item in file_list[i:]:
        if start_item in files_to_remove:
            i = i + 1
            continue            
        img1 = cv2.imread(start_item, 0)
        count = 0
        for comp_item in file_list[i+1:]:
            progress_string = "checking file " + str(i) + " of " + str(len(file_list)) + " against " + str(count) + " of " + str(len(file_list)-i) + " removing " + str(len(files_to_remove)) + " files\r"
            sys.stdout.write("\033[K")
            sys.stdout.write(progress_string)
            if comp_item in files_to_remove:
                continue
            img2 = cv2.imread(comp_item, 0)
            res = cv2.absdiff(img1, img2)
            res = res.astype(np.uint8)
            percentage = (np.count_nonzero(res) * 100)/ res.size
            if percentage < threshold:
                files_to_remove.append(comp_item)
            count = count + 1
        i = i + 1

    
        
num_args = len(sys.argv)
if num_args < 3:
  print ("USAGE: image_compare [source folder] [threshold]")
  sys.exit()

source_dir = sys.argv[1]
threshold = int(sys.argv[2])

compare_images(source_dir, threshold)
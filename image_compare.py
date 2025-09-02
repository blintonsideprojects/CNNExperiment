import cv2
import sys
import os
import numpy as np
from PIL import Image
import imagehash
import time

def remove_files(file_list):
    for item in file_list:
        os.remove(item)        

def get_files_to_compare(source_dir):
    all_files = []

    # recursively find all files in the given folder
    for root, subdirs, files in os.walk(source_dir):
        for filename in files:
            full_path = os.path.join(root, filename)
            all_files.append(full_path)
    
    return all_files
        
def process_file_group(file_group):
    pass

def compare_images_imagehash(source_dir, dest_dir, threshold, total_files):        
    num_files_removed = 1
    while num_files_removed >= 0:
        num_files_removed = 0
        file_list = get_files_to_compare(source_dir)
        if len(file_list) > 1:
            start_item = file_list[0]
            remove_list = []
            files_processed = 0
            start_time = time.perf_counter()
            for comp_item in file_list[1:]:
                progress_string = "Checking file " + str(files_processed+1) + " of " + str(len(file_list)) + " " + str(int((files_processed+1)/len(file_list)*100)) + "% removing " + str(len(remove_list)) + " files\r"
                sys.stdout.write("\033[K")                
                sys.stdout.write(progress_string)
                hash0 = imagehash.average_hash(Image.open(start_item))
                hash1 = imagehash.average_hash(Image.open(comp_item))
                hash_diff = hash0 - hash1
                if hash_diff < threshold:
                    remove_list.append(comp_item)
                files_processed = files_processed + 1
            num_files_removed = len(remove_list)
            remove_files(remove_list)            
            dest_path = os.path.join(dest_dir, os.path.basename(start_item))
            os.rename(start_item, dest_path)    
            end_time = time.perf_counter()
            processed_string = start_item + " has been processed in " + str(end_time-start_time) + " seconds."
            print(processed_string)         
    
num_args = len(sys.argv)
if num_args < 4:
  print ("USAGE: image_compare [source folder] [dest folder] [threshold]") 
  sys.exit()

source_dir = sys.argv[1]
dest_dir = sys.argv[2]
threshold = int(sys.argv[3])

all_files = get_files_to_compare(source_dir)
total_files = len(all_files)
compare_images_imagehash(source_dir, dest_dir, threshold, total_files)
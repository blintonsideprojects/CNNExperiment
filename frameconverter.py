import cv2
import sys
import os

def extract_frames(source_file, dest_path):
  count = 0
  success = True
  vidcap = cv2.VideoCapture(source_file)
  while success:
    success,image = vidcap.read()
    source_file_name = os.path.splitext(os.path.basename(source_file))
    dest_file_name = source_file_name[0] + "_frame_" + str(count) + ".png"
    final_dest = os.path.join(dest_path, dest_file_name)
    cv2.imwrite(final_dest, image)     # save frame as JPEG file      
    progress_string = "Processing frame #" + str(count) + "\r"
    sys.stdout.write(progress_string)
    count = count + 1

num_args = len(sys.argv)
if num_args < 3:
  print ("USAGE: frameconverter [source folder] [destination folder]")
  sys.exit()

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

for root, subdirs, files in os.walk(source_dir):
    for filename in files:
      file_path = os.path.join(root, filename)
      extract_frames(file_path, dest_dir)


#count = 0
#while success:
#  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
#  success,image = vidcap.read()
#  print('Read a new frame: ', success)
#  count += 1
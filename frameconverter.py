import cv2
import sys
import os

def count_frames(source_path):
  total_frames = 0
  for root, subdirs, files in os.walk(source_path):
    for filename in files:
      fname, file_extension = os.path.splitext(os.path.join(root, filename))
      if str.lower(file_extension) == ".mp4":
        vidcap = cv2.VideoCapture(os.path.join(root, filename))
        total_frames = total_frames + int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

  return total_frames

def extract_frames(source_path, dest_path):
  count = 0
  print ("Counting Frames Please Wait...")
  total_frames = count_frames(source_path)

  for root, subdirs, files in os.walk(source_path):
    for filename in files:
      success = True
      fname, file_extension = os.path.splitext(os.path.join(root, filename))
      if str.lower(file_extension) == ".mp4":
        vidcap = cv2.VideoCapture(os.path.join(root, filename))
        print (os.path.join(root, filename))
        if vidcap.isOpened():
          while success:
            success,image = vidcap.read()
            if not success:
              break
            source_file_name = os.path.splitext(os.path.basename(filename))
            dest_file_name = source_file_name[0] + "_frame_" + str(count) + ".png"
            final_dest = os.path.join(dest_path, dest_file_name)
            cv2.imwrite(final_dest, image)       
            progress_string = "Processing frame #" + str(count) + " of " + str(total_frames) + "\r"
            sys.stdout.write(progress_string)
            count = count + 1

num_args = len(sys.argv)
if num_args < 3:
  print ("USAGE: frameconverter [source folder] [destination folder]")
  sys.exit()

source_dir = sys.argv[1]
dest_dir = sys.argv[2]

extract_frames(source_dir, dest_dir)
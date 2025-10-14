
#FILE ORGANIZER


#Organizes files based on extension.

"""
USAGE:
Copy it to the folder that you want to oragnize and run the script
"""

import os
import shutil

srcdir = os.getcwd()
dstdir = srcdir

file_type = {
    '.jpg' : 'Images',
    '.jpeg' : 'Images',
    '.png' : 'Images',
    '.bmp' : 'Images',
    '.mp4' : 'Videos',
    '.mkv' : 'Videos',
    '.flv' : 'Videos',
    '.wmv' : 'Videos',
    '.pdf' : 'Documents',
    '.doc' : 'Documents',
    '.docx' : 'Documents',
    '.xls' : 'Documents',
    '.xlsx' : 'Documents',
    '.txt' : 'Documents',
    '.ppt' : 'Documents', 
    '.py' : 'Documents',
    '.js' : 'Documents',
    '.html' : 'Documents',
    '.php' : 'Documents',
    '.sh' : 'Documents',
    '.xml' : 'Documents',
    '.json' : 'Documents',
    '.csv' : 'Documents',
    '.der' : 'Documents',
    '.mp3' : 'Audio',
    '.wav' : 'Audio',
    '.zip' : 'Archives',
    '.rar' : 'Archives',
    '.7z' : 'Archives',
    '.tar' : 'Archives',
    '.xz' : 'Archives',
    '.gz' : 'Archives',
    '.bin' : 'Archives',
    '.iso' : 'Archives',
    '.exe' : 'Executables',
    '.deb' : 'Executables'
}

others = 'Others'

print("""
 ######  ####   ####   ####  #     # ####### ########  ####### #### 
#      # #   # #      #    # ##    #    #          #   #       #   #
#      # # ##  #      #    # # #   #    #         #    #       # ##
#      # ###   #      #    # #  #  #    #        #     ######  ###
#      # # #   #  ### ###### #   # #    #       #      #	   #  #
#      # #  #  #    # #    # #    ##    #      #       #       #   #
 ######  #   #  ##### #    # #     # #######  ######## ####### #    #

-------------------------By aluminium-----------------------------      
""")
print("\n[GITHUB] https://github.com/aluminium65/")




for files in os.listdir(srcdir):

  if files == 'organizer.py':
    continue

  print (f"Scanning all of the files in current directory.")

  srcpath = os.path.join(srcdir, files)

  if os.path.isdir(srcpath):
    continue

  filename, ext = os.path.splitext(files)

  if ext in file_type:
    folder = file_type[ext]

  else:
    folder = others

  dstpath = os.path.join(dstdir, folder)

  if not os.path.exists(dstpath):
    os.makedirs(dstpath)
    print (f"Created folder: \"{folder}\"")

  dstfilepath = os.path.join(dstpath, files)

  shutil.move(srcpath, dstfilepath)
  print (f"Moved \"{files}\" to \"{dstpath}\"")



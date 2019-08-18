# python3 assignment.py /home/rj/desktop file.txt
#
# This command should create a file file.txt at /home/rj/desktop.Hint:
# 1. use sys module &  sys.argv to capture the arguments passed from command line.
#
# PS. assignment.py is a file name
# @channel other 2 (two) are required arguments

import sys
import os

if len(sys.argv) == 3:

    os.chdir(sys.argv[1])
    os.mknod(sys.argv[2])
#!/usr/bin/python3

from os import listdir
from os.path import isfile, join
import sys
import pickle

mypath = sys.argv[1]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
pickle.dump(onlyfiles,open("files.txt","wb"))

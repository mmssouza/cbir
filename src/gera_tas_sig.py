#!/usr/bin/python

import sys
import scipy
import cPickle
import descritores

diretorio = sys.argv[1]

cl = cPickle.load(open(diretorio+"classes.txt","r"))
fnames = cPickle.load(open(diretorio+"names.pkl","r"))

db = {}

for im_file in fnames:
   tmp = descritores.TAS(diretorio+im_file)
   db[im_file] = scipy.hstack((cl[im_file],tmp.sig))
#   print im_file,db[im_file]
   
cPickle.dump(db,open(sys.argv[2],"w"))

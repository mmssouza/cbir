#!/usr/bin/python

import sys
import scipy
import cPickle
import descritores

diretorio = sys.argv[1]

f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = descritores.TAS(diretorio+im_file)
   db[im_file] = scipy.hstack((cl[im_file],tmp.sig))
#   print im_file,db[im_file]
   
cPickle.dump(db,open(sys.argv[2],"w"))

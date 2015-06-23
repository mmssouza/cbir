#!/usr/bin/python

import sys
import numpy as np
import cPickle
import descritores

diretorio = sys.argv[1]

f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = descritores.cd(diretorio+im_file)
   h = np.histogram(tmp,bins = 30,range = (0.05,1.))
   h = h[0].astype(float)/float(h[0].sum())
   print im_file,h
   db[im_file] = np.hstack((cl[im_file],h))
#   print im_file,db[im_file]
   
cPickle.dump(db,open(sys.argv[2],"w"))

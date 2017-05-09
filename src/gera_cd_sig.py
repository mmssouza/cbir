#!/usr/bin/python

import sys
import numpy as np
import cPickle
import descritores

diretorio = sys.argv[1]
bins = int(round(float(sys.argv[2])))
#rmin = float(sys.argv[3])
#rmax = float(sys.argv[4])

rmin = 0
rmax = 1.0
s = float(sys.argv[3])
#print "cd",bins,rmin,rmax

cl = cPickle.load(open(diretorio+"classes.txt","r"))
fnames = cPickle.load(open(diretorio+"names.pkl","r"))

db = {}

for im_file in fnames:
   tmp = descritores.cd(diretorio+im_file,sigma = s)
   h = np.histogram(tmp,bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
   
cPickle.dump(db,open(sys.argv[4],"w"))

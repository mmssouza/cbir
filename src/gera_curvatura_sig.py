#!/usr/bin/python

import sys
import numpy as np
import cPickle
import descritores as desc

diretorio = sys.argv[1]
sigma = float(sys.argv[2])
bins = int(round(float(sys.argv[3])))
rmin = float(sys.argv[4])
rmax = float(sys.argv[5])
print "curv",sigma,bins,rmin,rmax
f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = desc.curvatura(diretorio+im_file,np.array([sigma]))
   h = np.histogram(tmp.curvs[0],bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
#   print im_file,db[im_file]
   
cPickle.dump(db,open(sys.argv[6],"a"))

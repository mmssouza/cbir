#!/usr/bin/python

import sys
import cPickle
import numpy as np
import aii

diretorio = sys.argv[1]
area = float(sys.argv[2])
bins = int(round(float(sys.argv[3])))
rmin = float(sys.argv[4])
rmax = float(sys.argv[5])
print "aii",area,bins,rmin,rmax
f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = aii.AreaIntegralInvariant2(diretorio+im_file,area,0)
   h = np.histogram(tmp,bins = bins,range = (rmin*tmp.min(),rmax*tmp.max()))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
#   print im_file,db[im_file]
   
cPickle.dump(db,open(sys.argv[6],"a"))

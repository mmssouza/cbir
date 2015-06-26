#!/usr/bin/python

import sys
import numpy as np
import cPickle
import descritores

diretorio = sys.argv[1]
bins = int(round(float(sys.argv[2])))
rmin = float(sys.argv[3])
rmax = float(sys.argv[4])

f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = descritores.cd(diretorio+im_file)
   h = np.histogram(tmp,bins = 40,range = (0.1,1.))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
#   print im_file,db[im_file]
   
cPickle.dump(db,open(sys.argv[5],"a"))

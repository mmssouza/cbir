#!/usr/bin/python

import sys
import numpy as np
import cPickle
import descritores as desc

diretorio = sys.argv[1]
sigma = 25.

f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = desc.curvatura(diretorio+im_file,np.array([sigma]))
   h = np.histogram(tmp.curvs[0],bins = 30,range = (-1000.,1000.))
   h = h[0].astype(float)/float(h[0].sum())
   print im_file,h
   db[im_file] = np.hstack((cl[im_file],h))
#   print im_file,db[im_file]
   
cPickle.dump(db,open(sys.argv[2],"w"))
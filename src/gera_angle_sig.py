#!/usr/bin/python

import sys
import numpy as np
import cPickle
import descritores

diretorio = sys.argv[1]
raio = int(round(float(sys.argv[2])))
bins = int(round(float(sys.argv[3])))
rmin = float(sys.argv[4])
rmax = float(sys.argv[5])
s = float(sys.argv[6])
#print "angle",raio,bins,rmin,rmax
f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = descritores.angle_seq_signature(diretorio+im_file,raio,sigma = s)
   h = np.histogram(tmp.sig,bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
   
cPickle.dump(db,open(sys.argv[7],"a"))

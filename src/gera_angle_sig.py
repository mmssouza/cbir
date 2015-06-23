#!/usr/bin/python

import sys
import numpy as np
import cPickle
import descritores

diretorio = sys.argv[1]
raio = 30

f = open(diretorio+"classes.txt","r")
cl = cPickle.load(f)
f.close()

db = {}

for im_file in cl.keys():
   tmp = descritores.angle_seq_signature(diretorio+im_file,raio)
   h = np.histogram(tmp.sig,bins = 30,range = (0.,np.pi))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
   print im_file,h
#   print im_file,db[im_file]
   
cPickle.dump(db,open(sys.argv[2],"w"))

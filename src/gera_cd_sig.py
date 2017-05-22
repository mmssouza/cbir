#!/usr/bin/python3

import sys
import numpy as np
import pickle
import descritores

diretorio = sys.argv[1]
bins = int(round(float(sys.argv[2])))
#rmin = float(sys.argv[3])
#rmax = float(sys.argv[4])

rmin = 0
rmax = 1.0
s = float(sys.argv[3])
#print "cd",bins,rmin,rmax

cl = pickle.load(open(diretorio+"classes.txt","rb"))
fnames = pickle.load(open(diretorio+"names.pkl","rb"))

db = {}

for im_file in fnames:
   tmp = descritores.cd(diretorio+im_file,sigma = s)
   h = np.histogram(tmp,bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
   
pickle.dump(db,open(sys.argv[4],"wb"))

#!/usr/bin/python3

import sys
import numpy as np
import pickle
import descritores as desc

diretorio = sys.argv[1]
sigma = float(sys.argv[2])
bins = int(round(float(sys.argv[3])))
rmin = float(sys.argv[4])
rmax = float(sys.argv[5])
#print "curv",sigma,bins,rmin,rmax
cl = pickle.load(open(diretorio+"classes.txt","rb"))
fnames = pickle.load(open(diretorio+"names.pkl","rb"))
db = {}

for im_file in fnames:
   tmp = desc.curvatura(diretorio+im_file,np.array([sigma]))
   h = np.histogram(tmp.curvs[0],bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
#   print im_file,db[im_file]
   
pickle.dump(db,open(sys.argv[6],"wb"))

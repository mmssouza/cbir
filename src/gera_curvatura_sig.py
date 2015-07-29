#!/usr/bin/python

import numpy as np
import tempfile
import cPickle
import descritores as desc

def gera_curvatura_sig(diretorio,args,cl):
 sigma = args[0]
 bins = int(round(args[1]))
 rmin = args[2]
 rmax = args[3]
 
 db = {}

 for im_file in cl.keys():
   tmp = desc.curvatura(diretorio+im_file,np.array([sigma]))
   h = np.histogram(tmp.curvs[0],bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
#   print im_file,db[im_file]
 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)        
 cPickle.dump(db,tmp0)
 return tmp0.name


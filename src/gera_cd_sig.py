#!/usr/bin/python

import numpy as np
import tempfile
import cPickle
import descritores

def gera_cd_sig(diretorio,args,cl):
 bins = int(round(args[0]))
 rmin = args[1]
 rmax = args[2]
 s = args[3]
 
 db = {}

 for im_file in cl.keys():
   tmp = descritores.cd(diretorio+im_file,sigma = s)
   h = np.histogram(tmp,bins = 40,range = (0.1,1.))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
#   print im_file,db[im_file]
 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)     
 cPickle.dump(db,tmp0)
 return tmp0.name


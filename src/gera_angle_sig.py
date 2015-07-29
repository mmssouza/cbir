#!/usr/bin/python

import numpy as np
import cPickle
import tempfile
import descritores


def gera_angle_sig(diretorio,args,cl):
 raio = int(round(args[0]))
 bins = int(round(args[1]))
 rmin = args[2]
 rmax = args[3]
 s = args[4]
 
 db = {}

 for im_file in cl.keys():
   tmp = descritores.angle_seq_signature(diretorio+im_file,raio,sigma = s)
   h = np.histogram(tmp.sig,bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))

 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)   
 cPickle.dump(db,tmp0)
 return tmp0.name


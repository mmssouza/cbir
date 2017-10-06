
import numpy as np
import pickle
import tempfile
import descritores
import settings


def gera_angle_sig(cl,args,cntr_dict):
 bins = int(round(args[0]))
 rmin = 0.
 rmax = 1.
 s = args[1]
 r = args[2]
 
 db = {}

 for im_file in iter(cntr_dict):
   tmp = descritores.angle_seq_signature(cntr_dict[im_file],r,sigma = s)
   h = np.histogram(tmp.sig,bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
   
 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir=settings.tmp_path,delete = False)   
 pickle.dump(db,tmp0)
 
 return tmp0.name


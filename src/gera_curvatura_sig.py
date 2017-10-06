
import numpy as np
import tempfile
import pickle
import descritores as desc
import settings

def gera_curvatura_sig(cl,args,cntr_dict):
 sigma = args[0]
 bins = int(round(args[1]))
 rmin = -1.
 rmax = 1.
 
 db = {}

 for im_file in iter(cntr_dict.keys()):
   tmp = desc.curvatura(cntr_dict[im_file],np.array([sigma]))
   h = np.histogram(tmp.curvs[0],bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   db[im_file] = np.hstack((cl[im_file],h))
   
 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir=settings.tmp_path,delete = False)        
 pickle.dump(db,tmp0)
 return tmp0.name

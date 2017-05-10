import numpy as np
import tempfile
import pickle
import descritores

def gera_cd_sig(diretorio,args):
 bins = int(round(args[0]))
 rmin = 0.
 rmax = 1.
 s = args[1]
 
 db = {}
 cl = pickle.load(open(diretorio+"classes.txt","rb"))
 fnames = pickle.load(open(diretorio+"names.pkl","rb"))

 for im_file in fnames:
  tmp = descritores.cd(diretorio+im_file,sigma = s)
  h = np.histogram(tmp,bins = bins,range = (rmin,rmax))
  h = h[0].astype(float)/float(h[0].sum())
  db[im_file] = np.hstack((cl[im_file],h))
  
 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)     
 pickle.dump(db,tmp0)
 return tmp0.name

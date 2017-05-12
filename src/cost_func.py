
import os
from gera_angle_sig import gera_angle_sig 
from gera_cd_sig import gera_cd_sig
from gera_curvatura_sig import gera_curvatura_sig
from rank40_mt import rank40
#from rank40 import rank40
from multiprocessing import Queue,Process
from descritores import contour_base
import pickle

diretorio = '../leaves_png/'

fnames = pickle.load(open(diretorio+"names.pkl","rb"))
cl = pickle.load(open(diretorio+"classes.txt","rb"))
contours = [contour_base(diretorio+fn).c for fn in fnames]

def worker(in_q,out_q):
  args = in_q.get()
  f = args[0]
  out_q.put(f(cl,args[1],dict(zip(fnames,contours))))


def cost_func(args):

 curv_args = args[0:4]
 angle_args = args[4:7]
 cd_args = args[7:9]
 rank_args = args[9:12]
 
 in_q,out_q = Queue(),Queue()

# print "passo 1 - Extracao caracteristicas"
 
 threads = []
 for i in range(3):
  t =  Process(target=worker,args=(in_q,out_q))
  threads.append(t)

 for p in threads:
  p.start()
 
 in_q.put([gera_angle_sig,angle_args])
 in_q.put([gera_cd_sig,cd_args])
 in_q.put([gera_curvatura_sig,curv_args])

 for p in threads:
  p.join()
  
 tmp0 = out_q.get()
 tmp1 = out_q.get()
 tmp2 = out_q.get()
 
 
# print "passo 2 - Bull eye"
 res = rank40(tmp0,tmp1,tmp2,rank_args)

 os.remove(tmp0)
 os.remove(tmp1)
 os.remove(tmp2)

 return res

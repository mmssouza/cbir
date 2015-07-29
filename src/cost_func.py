#!/usr/bin/python

import cPickle
import os
import numpy as np
from gera_aii_sig_mt import gera_aii_sig_mt
from gera_angle_sig import gera_angle_sig 
from gera_cd_sig import gera_cd_sig
from gera_curvatura_sig import gera_curvatura_sig
from rank40_mt import rank40_mt
from multiprocessing import Queue,Process

diretorio = '../../1400_mpeg7_Preprocessadas/'

def worker(in_q,out_q):
  args = in_q.get()
  f = args[0]
  cl = args[2]
  out_q.put(f(diretorio,args[1],cl))


def cost_func(args):

 aii_args = args[0:4]
 curv_args = args[4:8]
 angle_args = args[8:13]
 cd_args = args[13:17]
 with open(diretorio+"classes.txt","r") as f:
  cl = cPickle.load(f)

 in_q,out_q = Queue(),Queue()

# print "passo 1 - Extracao caracteristicas"
 
 threads = []
 for i in range(4):
  t =  Process(target=worker,args=(in_q,out_q))
  threads.append(t)

 for p in threads:
  p.start()
 
 in_q.put([gera_aii_sig_mt,aii_args,cl])
 in_q.put([gera_angle_sig,angle_args,cl])
 in_q.put([gera_cd_sig,cd_args,cl])
 in_q.put([gera_curvatura_sig,curv_args,cl])

 tmp0 = out_q.get()
 tmp1 = out_q.get()
 tmp2 = out_q.get()
 tmp3 = out_q.get()
 
# print "passo 2 - Bull eye"
 res = rank40_mt(tmp0,tmp1,tmp2,tmp3)

 os.remove(tmp0)
 os.remove(tmp1)
 os.remove(tmp2)
 os.remove(tmp3)

 return res



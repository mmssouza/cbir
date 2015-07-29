#!/usr/bin/python

import cPickle
import numpy as np
import tempfile
import aii
from multiprocessing import Queue,Process

def worker(diretorio,area,bins,rmin,rmax,cl,in_q,out_q):
  f_list = in_q.get()
  d = {}
  for im_file in f_list:
   tmp = aii.AreaIntegralInvariant2(diretorio+im_file,area,0)
   h = np.histogram(tmp,bins = bins,range = (rmin,rmax))
   h = h[0].astype(float)/float(h[0].sum())
   d[im_file] = np.hstack((cl[im_file],h))
  out_q.put(d)


def gera_aii_sig_mt(diretorio,args,cl):

 area = args[0]
 bins = int(round(args[1]))
 rmin = args[2]
 rmax = args[3]

 in_q,out_q = Queue(),Queue()

 threads = []
 for i in range(7):
  t =  Process(target=worker,args=(diretorio,area,bins,rmin,rmax,cl,in_q,out_q))
  threads.append(t)

 for p in threads:
  p.start()
 
 in_q.put(cl.keys()[0:200])
 in_q.put(cl.keys()[200:400])
 in_q.put(cl.keys()[400:600])
 in_q.put(cl.keys()[600:800])
 in_q.put(cl.keys()[800:1000])
 in_q.put(cl.keys()[1000:1200])
 in_q.put(cl.keys()[1200:1400])

 d = []
 d.append(out_q.get())
 d.append(out_q.get())
 d.append(out_q.get())
 d.append(out_q.get())
 d.append(out_q.get())
 d.append(out_q.get())
 d.append(out_q.get())

 dall = {}
 for i in d:
  dall.update(i)
 
 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 cPickle.dump(dall,tmp0)

 return tmp0.name

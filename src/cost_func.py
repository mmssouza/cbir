#!/usr/bin/python

import subprocess
import shlex
import tempfile
import os
import cStringIO
import numpy as np

def cost_func(args):

 args = shlex.split(str(args.tolist()).lstrip('[').rstrip(']'))
 args = [a.strip(',') for a in args]

 aii_args = args[0:4]
 curv_args = args[4:8]
 angle_args = args[8:12]
 cd_args = args[12:15]

 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 tmp1 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 tmp2 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 tmp3 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 print "passo 1 - Extracao caracteristicas"
 p_aii = subprocess.Popen(['./gera_aii_sig_mt.py','../../1400_mpeg7_Preprocessadas/']+aii_args+[tmp0.name])
 p_curv = subprocess.Popen(['./gera_curvatura_sig.py','../../1400_mpeg7_Preprocessadas/']+curv_args+[tmp1.name])
 p_angle = subprocess.Popen(['./gera_angle_sig.py','../../1400_mpeg7_Preprocessadas/']+angle_args+[tmp2.name])
 p_cd = subprocess.Popen(['./gera_cd_sig.py','../../1400_mpeg7_Preprocessadas/']+cd_args+[tmp3.name])

 p_cd.wait()
 p_angle.wait()
 p_curv.wait()
 p_aii.wait()
  
 print "passo 2 - Bull eye"
 out = cStringIO.StringIO(); 
 res = subprocess.check_output(['./rank40_mt.py',tmp0.name,tmp1.name,tmp2.name,tmp3.name])
 os.remove(tmp0.name)
 os.remove(tmp1.name)
 os.remove(tmp2.name)
 print res
 return float(res)



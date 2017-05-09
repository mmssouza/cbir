#!/usr/bin/python

import subprocess
import shlex
import tempfile
import os

def cost_func(args):

 args = shlex.split(str(args.tolist()).lstrip('[').rstrip(']'))
 args = [a.strip(',') for a in args]

 #aii_args = args[0:4]
 #curv_args = args[4:8]
 #angle_args = args[8:13]
 #cd_args = args[13:17]
 
 curv_args = args[0:4]
 angle_args = args[4:6]
 cd_args = args[6:8]
 rank_args = args[8:11]
 
 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 tmp1 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 tmp2 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 
#print "passo 1 - Extracao caracteristicas"
 p_curv = subprocess.Popen(['./gera_curvatura_sig.py','../leaves_160_png/']+curv_args+[tmp0.name])
 p_angle = subprocess.Popen(['./gera_angle_sig.py','../leaves_160_png/']+angle_args+[tmp1.name])
 p_cd = subprocess.Popen(['./gera_cd_sig.py','../leaves_160_png/']+cd_args+[tmp2.name])

 p_cd.wait()
 p_angle.wait()
 p_curv.wait()
  
# print "passo 2 - Bull eye"
 res = subprocess.check_output(['./rank40.py',tmp0.name,tmp1.name,tmp2.name]+rank_args)
 os.remove(tmp0.name)
 os.remove(tmp1.name)
 os.remove(tmp2.name)
# print res
 return float(res)



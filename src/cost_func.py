#!/usr/bin/python

import subprocess
import shlex
import tempfile
import os
import cStringIO

def cost_func(args):

 args = shlex.split(args)
 aii_args = args[0:4]
 curv_args = args[4:8]
 angle_args = args[8:12]
 cd_args = args[12:15]

 tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 tmp1 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 tmp2 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 tmp3 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)

 p_aii = subprocess.Popen(['./gera_aii_sig.py','../../1400_mpeg7_Preprocessadas/']+aii_args+[tmp0.name])
 p_curv = subprocess.Popen(['./gera_curvatura_sig.py','../../1400_mpeg7_Preprocessadas/']+curv_args+[tmp1.name])
 p_angle = subprocess.Popen(['./gera_angle_sig.py','../../1400_mpeg7_Preprocessadas/']+angle_args+[tmp2.name])
 p_cd = subprocess.Popen(['./gera_cd_sig.py','../../1400_mpeg7_Preprocessadas/']+cd_args+[tmp3.name])
 p_aii.wait()
 p_curv.wait()
 p_angle.wait()
 p_cd.wait() 
 
 out = cStringIO.StringIO(); 
 res = subprocess.check_output(['./rank40_mt.py',tmp0.name,tmp1.name,tmp2.name,tmp3.name])
 os.remove(tmp0.name)
 os.remove(tmp1.name)
 os.remove(tmp2.name)
 return float(res)

cost_func('0.15 25 0.1 1.0 27.0 30 -2000 2000 20 10 0.15 3.14 10 0.1 1.0')


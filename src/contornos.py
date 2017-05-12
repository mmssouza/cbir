#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-
import sys
import pylab
import pickle
import descritores as desc
d = sys.argv[1]
dd = sys.argv[2]
f = open(d+"classes.txt","rb")
nomes = pickle.load(f).keys()
f.close()
pylab.figure(1)
for fname in iter(nomes):
 print(fname)  
 c = desc.contour_base(d+fname).c
 pylab.scatter(pylab.array([i.real for i in c]),pylab.array([i.imag for i in c]),s = 5)
 pylab.savefig(dd+fname)
 pylab.cla()

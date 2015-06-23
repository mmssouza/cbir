#!/usr/bin/python
import scipy
import cPickle
import pylab
import sys

f = open(sys.argv[1])
d = cPickle.load(f)
f.close()
cl = scipy.array([d[k][0] for k in d.keys()])
f = open(sys.argv[2])
l = cPickle.load(f)
dd = cPickle.load(f)
dd = dd[0]
l = []
for i in scipy.arange(1,cl.max()+1):
 daux1 = dd[cl == i]
 laux = []
 for j in scipy.arange(1,cl.max()+1):
   daux2 = daux1.transpose()[cl == j]
   laux.append(daux2)
 l.append(scipy.hstack(laux))

dd = scipy.vstack(l)

pylab.imshow(dd*255)
pylab.show()


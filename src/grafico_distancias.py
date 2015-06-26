#!/usr/bin/python

import scipy
import pylab
import jsd
import hellinger
import chi_square
import Patrick_Fisher

p = scipy.array([0.5,0.5])
t = scipy.arange(0.,1.05,0.05)
q = [scipy.array([a,1-a]) for a in t]

djs = scipy.array([jsd.jsd(p,u) for u in q])
dhe = scipy.array([hellinger.He(p,u) for u in q])
dcs = scipy.array([chi_square.chi_square(p,u) for u in q])
dpf = scipy.array([Patrick_Fisher.Patrick_Fisher(p,u) for u in q])

for a,b,c,d,e in zip(t,djs,dhe,dcs,dpf):
 print a,b,c,d,e

pylab.plot(t,djs)
pylab.plot(t,dhe)
pylab.plot(t,dcs)
pylab.plot(t,dpf)
pylab.show()

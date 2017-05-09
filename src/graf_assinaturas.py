#!/usr/bin/python

import pylab
import descritores
path = "../leaves_160_png/"
#leaves = ["1453.png","1480.png"]
#leaves = ["1211.png","1253.png"]
leaves = ["2045.png","2015.png"]
lt = ["k-","k--"]
label=["i1453","i1480"]
pylab.tick_params(direction='out', length=6, width=2, labelsize="large")

for i in enumerate(leaves):
 idx = i[0]
 d1 = descritores.curvatura(path+i[1],pylab.array([25.0])).curvs[0]
 t = pylab.linspace(0.,1.,d1.size)
 pylab.xlim((0,1.2))
 pylab.plot(t,d1,lt[idx],label=label[idx],linewidth=1.8)

legend = pylab.legend(loc=(0.7,0.6),frameon=False,labelspacing=2.8,borderpad = 1.0, fontsize='x-large')
pylab.savefig("graf_assinaturas_curv.png",dpi=200)
pylab.show()

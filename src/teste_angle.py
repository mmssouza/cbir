#!/usr/bin/python
import descritores as desc
import pylab
import numpy as np
import timeit

#start = timeit.default_timer()
l1 = desc.angle_seq_signature("../imagens/dude1.png",15)
l2 = desc.angle_seq_signature("../imagens/dude1_big.png",15)
l3 = desc.angle_seq_signature("../imagens/dude1_small.png",15)

pylab.subplot(311)
pylab.plot(l1.sig)
pylab.subplot(312)
pylab.plot(l2.sig)
pylab.subplot(313)
pylab.plot(l3.sig)

pylab.show()

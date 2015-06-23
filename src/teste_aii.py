import aii
import pylab
import timeit

#start = timeit.default_timer()
l1 = aii.AreaIntegralInvariant2("..\\imagens\\dude1.png",0.85)
l2 = aii.AreaIntegralInvariant2("..\\imagens\\dude1_big.png",0.85)
l3 = aii.AreaIntegralInvariant2("..\\imagens\\dude1_small.png",0.85)

pylab.subplot(311)
pylab.plot(l1)
pylab.subplot(312)
pylab.plot(l2)
pylab.subplot(313)
pylab.plot(l3)

pylab.show()
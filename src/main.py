#!/usr/bin/python -u
# -*- coding: utf-8 -*-
import depso
import cost_func

a = depso.de(fitness_func=cost_func.cost_func,npop = 17,pr = 0.75,beta = 3.5)

print a.fit.min(),a.fit.mean(),a.fit.max()
print a.pop[a.fit.argmax()]
print

for i in range(15):
 a.run()
 print i,a.fit.min(),a.fit.mean(),a.fit.max()
 print a.pop[a.fit.argmax()]
 print

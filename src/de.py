#!/usr/bin/python -u
# -*- coding: utf-8 -*-
import optimize
import cost_func

a = optimize.de(fitness_func=cost_func.cost_func,npop = 40,pr = 0.3,beta = .65)

print a.fit.min(),a.fit.mean(),a.fit.max()
print a.pop[a.fit.argmax()]
print

for i in range(100):
 a.run()
 print i,a.fit.min(),a.fit.mean(),a.fit.max()
 print a.pop[a.fit.argmax()]
 print

#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import optimize
import cost_func
import settings

if settings.algo == "sa":
 T = settings.params[0]
 alpha = settings.params[1]
 P = settings.params[2]
 L = settings.params[3]
 a = optimize.sim_ann(cost_func.cost_func,T,alpha,P,L)

 for i in range(settings.Niter):
  a.run()
  print(i,a.fit)
  print(a.s)
  print()
elif settings.algo == "de":
 Npop = settings.params[0]
 Pr = settings.params[1]
 Beta = settings.params[2]   
 a = optimize.de(cost_func.cost_func,Npop,Pr,Beta)
 for i in range(settings.Niter):
  a.run()
  print(i,a.fit.min(),a.fit.mean(),a.fit.max())
  print(a.pop[a.fit.argmax()])
  print()

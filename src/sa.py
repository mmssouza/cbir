#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
import optimize
import cost_func

a = optimize.sim_ann(cost_func.cost_func,90,0.9,6,3)

for i in range(136):
 a.run()
 print(i,a.s)
 print(a.fit)
 print()

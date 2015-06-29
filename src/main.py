#!/usr/bin/python

import depso
import cost_func

a = depso.de(fitness_func=cost_func.cost_func)
print a.pop
print a.fit

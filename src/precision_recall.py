#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import cPickle
import scipy
import PrecisionByRecall
import pylab

l = cPickle.load(open(sys.argv[1]))
r = PrecisionByRecall.PrecisionByRecall(l,20)

for i,j in zip(r.recall,r.precision):
 print i,j


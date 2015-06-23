# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:51:42 2013

@author: Ismael
"""
from __future__ import division

class PrecisionByRecall(object):
        
    def __init__(self,array,relevants):  
        recall = range(1,relevants+1)
        self.recall = [x/relevants for x in recall]
        self.precision = []
        for i in range(0,relevants ):
            self.precision.insert(i,sum(array[:,i])/array.size)         

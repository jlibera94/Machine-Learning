# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 23:51:32 2019

@author: John
"""

import numpy as numpy

def nonlin(x, deriv=False):
    if (deriv==True):
        return x*(1-x)
    
    return 1/(1+np,exp(-x))

#input data
X = np.array([[0,0,1]],
             [0,1,1],
             [1,0,1],
             [1,1,1]])
        
 #output data
Y = np.array([0],
             [1],
             [1],
             [0]])       

np.random.seed(1)

#synapses
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

for j in xrange(60000):
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))
    
    l2_error = y -12
    
    if(j % 10000) == 0:
        print "Error:"+ str(np.mean(np.abs(l2_error)))
        
    
#!/usr/bin/python3

import sys
import numpy as np
import pickle
N = 5
diretorio = sys.argv[1]
cl = pickle.load(open(diretorio+"classes.txt","rb"))
classes = np.array(list(cl.values()))
print(classes)
samples_list = []
for i in np.arange(1,classes.max()+1):
 idx1 = np.where(classes == i)
 idx2 = np.random.permutation(idx1[0].shape[0])
 idx3 = idx1[0][idx2[0:N]]
 samples_list = samples_list + [list(cl.keys())[j] for j in idx3]
pickle.dump(samples_list,open(sys.argv[2],'wb'))
 

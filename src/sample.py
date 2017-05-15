#!/usr/bin/python3

import pickle
import scipy
from numpy.random import permutation

classes = 32
spc = 50
dir ="../leaves_png/"
db = pickle.load(open(dir+"classes.txt","rb"))
cl = scipy.array([c for c in iter(db.values())])
k = scipy.array([k for k in iter(db.keys())])
l = []
for i in range(1,classes+1):
 l.append(k[cl == i])

ll = []
for i in l:
 ll = ll + permutation(i[0:spc]).tolist()

pickle.dump(ll,open("names.pkl","wb"))


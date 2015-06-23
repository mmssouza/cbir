#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import cStringIO
#import math
import cPickle
import numpy as np
import scipy
#import jsd
import hellinger as He

def pdist(X,dist_func):
 w1,w2,w3,w4 = (0.25,0.25,0.25,0.25)
 N = X.shape[0]
 p = scipy.zeros((N,N))
 for i,a in zip(scipy.arange(N),X):
   for j,b in zip(scipy.arange(i,N),X[i:]):
    p_a = np.histogram(a[0],bins = 35,range = (-1.,1.),normed = True)[0]
    p_b = np.histogram(b[0],bins = 35,range = (-1.,1.),normed = True)[0]
    d1 = dist_func(p_a,p_b)
    p_a = np.histogram(a[1],bins = 30,range = (0.,np.pi),normed = True)[0]
    p_b = np.histogram(b[1],bins = 30,range = (0.,np.pi),normed = True)[0]
    d2 = dist_func(p_a,p_b)
    p_a = np.histogram(a[2],bins = 15,range = (0.,1.),normed = True)[0]
    p_b = np.histogram(b[2],bins = 15,range = (0.,1.),normed = True)[0]
    d3 = dist_func(p_a,p_b)
    p_a = np.histogram(a[3],bins = 15,range = (0.2,0.8),normed = True)[0]
    p_b = np.histogram(b[3],bins = 15,range = (0.2,0.8),normed = True)[0]
    d4 = dist_func(p_a,p_b)
   
    p[i,j] = w1*d1+w2*d2+w3*d3+w4*d4
#    p[i,j] = np.min([d1,d2])
 p = p + p.transpose()
 return p

# parametros
db1 = cPickle.load(open(sys.argv[1]))
db2 = cPickle.load(open(sys.argv[2]))
db3 = cPickle.load(open(sys.argv[3]))
db4 = cPickle.load(open(sys.argv[4]))

# nome das figuras
name_arr = scipy.array(db1.keys())

# dicionario nome das figuras - classes
cl = dict(zip(name_arr,[int(db1[i][0]) for i in name_arr]))

# vetores de caracteristicas e classes
data = scipy.array([[db1[nome][1:],db2[nome][1:],db3[nome][1:],db4[nome][1:]] for nome in name_arr])
# distancia : medida de dissimilaridade a ser empregada 
#distancias = ['braycurtis','canberra','chebyshev','cityblock','correlation',
#              'cosine','dice','euclidean','hamming','jaccard',
#              'kulsinski','mahalanobis','matching','minkowski',
#              'rogerstanimoto','russelrao','seuclidean','sokalmichener',
#              'sokalsneath','sqeuclidean','yule']

#distancia = jsd.jsd
distancia = He.He
# Numero de amostras
Nobj = data.shape[0]

# numero de features
#Nfe = data.shape[1]

# Total de classes
Nclasses = max(cl.values())

# Total de amostras por classe
# assumindo que a base e balanceada!!!!
Nac = Nobj/Nclasses

# Numero de recuperacoes
Nretr = Nac

# Buffer para saida dos resultados
ots = cStringIO.StringIO() 

# Calcula matriz de distancias 
md = pdist(data,distancia)
l = []
for i,nome in zip(scipy.arange(Nobj),name_arr):
# Para cada linha de md estabelece rank de recuperacao
# O primeiro elemento de cada linha corresponde a forma modelo
# Obtem a classe dos objetos recuperados pelo ordem crescente de distancia
 idx = scipy.argsort(md[i])
 # pega classes a qual pertencem o primeiro padrao e as imagens recuperadas
 classe_padrao = cl[nome]
 name_retr = name_arr[idx] 
 aux = [cl[j] for j in name_retr]
 #output.write(classe_padrao)
 # estamos interessados apenas nos Nretr subsequentes resultados
 classe_retrs = aux[1:Nretr]
 n = scipy.nonzero(scipy.array(classe_retrs) == classe_padrao)
 tp = float(n[0].size)/float(scipy.array(classe_retrs).size)
 # Avalia e despeja resultados na saida
 l.append(scipy.array([classe_padrao,tp]))
 ots.write("{0} ".format(classe_padrao))
 for f in name_retr[0:11]:
  ots.write("{0} ".format(f))
 #ots.write(" {0}\n\n".format(tp))
 ots.write("\n")

l = scipy.array(l)

for c in scipy.arange(1,Nclasses+1):
 idx = scipy.nonzero(l[:,0] == c)
 print idx
 m = l[idx,1].mean()
 s = l[idx,1].std()
 ots.write("{0} {1} {2}\n".format(c,m,s))

ots.write("\n{0} {1}\n".format(scipy.mean(l[:,1]),scipy.std(l[:,1])))  

print ots.getvalue()  

ots.close()

#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
#import math
import cPickle
import numpy as np
import scipy
import jsd
import hellinger as He
import Patrick_Fisher as pf
import chi_square
import dkl

def pdist(X,dist_func):
 w1,w2,w3 = (0.45,0.45,0.1)
 N = X.shape[0]
 p = scipy.zeros((N,N))
 for i,a in zip(scipy.arange(N),X):
   for j,b in zip(scipy.arange(i,N),X[i:]):
    d1 = dist_func(a[0],b[0])
    d2 = dist_func(a[1],b[1])
    d3 = dist_func(a[2],b[2])
   
    p[i,j] = w1*d1+w2*d2+w3*d3
#    p[i,j] = np.min([d1,d2])
 p = p + p.transpose()
 return p

# parametros
db1 = cPickle.load(open(sys.argv[1]))
db2 = cPickle.load(open(sys.argv[2]))
db3 = cPickle.load(open(sys.argv[3]))

# nome das figuras
name_arr = scipy.array(db1.keys())

# dicionario nome das figuras - classes
cl = dict(zip(name_arr,[int(db1[i][0]) for i in name_arr]))

# vetores de caracteristicas e classes
data = scipy.array([[db1[nome][1:],db2[nome][1:],db3[nome][1:]] for nome in name_arr])

##################################################
# TEM DE ESPECIFICAR AQUI QUAL DISTANCIA UTILIZAR
#####################################3############

# Jensen-Shannon divergence
#distancia = jsd.jsd

# Chi square
#distancia = chi_square.chi_square

# Kullback Leiben
#distancia = dkl.D_KL

# Patrick Fisher
#distancia = pf.Patrick_Fisher

# Hellinger divergence
distancia = He.He

##########################################
# Numero de amostras da base
##########################################
Nobj = data.shape[0]

# Total de classes
Nclasses = max(cl.values())

# Total de amostras por classe
# assumindo que a base e balanceada!!!!
Nac = Nobj/Nclasses

# Numero de recuperacoes
Nretr = Nac

# Calcula matriz de distancias 
md = pdist(data,distancia)
# Para contabilizar a Matriz de confusão
l = scipy.zeros((Nclasses,Nac),dtype = int)

for i,nome in zip(scipy.arange(Nobj),name_arr):
# Para cada linha de md estabelece rank de recuperacao
# O primeiro elemento de cada linha corresponde a forma modelo
# Obtem a classe dos objetos recuperados pelo ordem crescente de distancia
  idx = scipy.argsort(md[i])
 # pega classes a qual pertencem o primeiro padrao e as imagens recuperadas
  classe_padrao = cl[nome]
  name_retr = name_arr[idx] 
  aux = scipy.array([cl[j] for j in name_retr])
 # estamos interessados apenas nos Nretr subsequentes resultados
  classe_retrs = aux[0:Nretr]
  n = scipy.nonzero(classe_retrs == classe_padrao)
 # Contabiliza resultados
  for i in n[0]:
   l[classe_padrao-1,i] = l[classe_padrao-1,i] + 1 

print(l.sum(axis = 0))

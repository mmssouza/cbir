#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import cPickle
import scipy
# Jensen-shannon divergence
#import jsd
# Hellinger distance
import hellinger as He
# Patrick Fisher
#import Patrick_Fisher as pf
#import chi_square
#import dkl
# Calcula matriz de distâncias
# Recebe como parâmetro as assinaturas
# e uma função para o cálculo de distâncias
def pdist(X,dist_func):
# pesos das caracteristicas para o cálculo da distância 
 N = X.shape[0]
 p = scipy.zeros((N,N))
 for i,a in zip(scipy.arange(N),X):
   for j,b in zip(scipy.arange(i,N),X[i:]):
    # Curvatura
    d1 = dist_func(a[0],b[0])
    # angle signature
    d2 = dist_func(a[1],b[1])
    # Centroid distance
    d3 = dist_func(a[2],b[2])
    # Area integral invariant
    d4 = dist_func(a[3],b[3])
    # distância da forma i para a forma j
    #p[i,j] = d1+d2+d3+d4
    p[i,j] = 0.45*d1+0.45*d2+0.1*d3
 p = p + p.transpose()
 return p

print "abrindo databases"
# databases
# Curvaturas
db1 = cPickle.load(open(sys.argv[1]))
# Angle sequence signature
db2 = cPickle.load(open(sys.argv[2]))
# Centroid distance
db3 = cPickle.load(open(sys.argv[3]))
# Area integral invariant
db4 = cPickle.load(open(sys.argv[4]))

# nome das figuras
name_arr = scipy.array(db1.keys())

# dicionario nome das figuras - classes
cl = dict(zip(name_arr,[db1[n][0] for n in name_arr]))

print "gerando base de histogramas"
# vetores de caracteristicas e classes
#data = scipy.array([scipy.fromstring(db[nome],sep=' ')[0:70] for nome in name_arr])
data = scipy.array([[db1[n][1:],db2[n][1:],db3[n][1:],db4[n][1:]] for n in name_arr])

# distancia : medida de dissimilaridade a ser empregada 
#distancias = ['braycurtis','canberra','chebyshev','cityblock','correlation',
#              'cosine','dice','euclidean','hamming','jaccard',
#              'kulsinski','mahalanobis','matching','minkowski',
#              'rogerstanimoto','russelrao','seuclidean','sokalmichener',
#              'sokalsneath','sqeuclidean','yule']

# Jensen-Shannon divergence
#distancia = dkl.D_KL
# Hellinger divergence
distancia = He.He

# Numero de amostras
Nobj = data.shape[0]

# Numero de recuperacoes para o cálculo do Bull eye
Nretr = 10

# Acumulador para contabilizar desempenho do experimento
tt = 0

# Calcula matriz de distancias 
print "Calculando matriz de distancias"
md = pdist(data,distancia)

print "Calculando bull eye score"
for i,nome in zip(scipy.arange(Nobj),name_arr):
 # Para cada linha de md estabelece rank de recuperação
 # ordenando a linha em ordem crescente de similaridade 
 # O primeiro elemento da linha corresponde a forma modelo
  idx = scipy.argsort(md[i])
 # pega classe a qual pertence a imagem modelo
  classe_padrao = cl[nome]
# nome das imagens recuperadas em ordem crescente de similaridade
  name_retr = name_arr[idx]
 # pega classes a qual pertencem as imagens recuperadas
  aux = [cl[j] for j in name_retr]
  # estamos interessados apenas nos Nretr (40) resultados
  classe_retrs = aux[0:Nretr]
  # Contabiliza desempenho contando o número de formas da mesma classe
  # do modelo (tp) dentre as 40 recuperadas
  # Atualiza o resultado acumulado (tt)
  n = scipy.nonzero(scipy.array(classe_retrs) == classe_padrao)
  tp = float(n[0].size)
  tt = tt + tp
    
# Bull eye
print 100*tt/float(160*5)  


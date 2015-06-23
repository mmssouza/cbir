#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import cPickle
import scipy
import PrecisionByRecall
import pylab
from scipy.spatial.distance import pdist,squareform

# Esta função recebe como parâmetro uma base de dados de vetores de características de imagens,  
# realiza o experimento CBIR e retorna como saída a matriz de confusão e o número de amostras por classe  
# A base de dados de entrada é um dicionário.
# db.keys() retorna em uma lista os nomes das imagens utilizadas para indexar o dicionário.
# O dicionário armazena, para cada imagem, os rótulos das classes na coluna 0 
# e os vetores de características nas demais colunas.
def Experimento(db):
# nome das figuras
 name_arr = scipy.array(db.keys())

# outro dicionario: nome das figuras x rótulos das classes
 cl = dict(zip(name_arr,[int(db[i][0]) for i in name_arr]))

# Obtém da base de entrada uma Matriz N_Samples x N_Features
# Descarta primeira coluna (Rótulos das classes)
 data = scipy.array([db[nome][1:] for nome in name_arr])

# distancia : medida de dissimilaridade a ser empregada 
#distancias = ['braycurtis','canberra','chebyshev','cityblock','correlation',
#              'cosine','dice','euclidean','hamming','jaccard',
#              'kulsinski','mahalanobis','matching','minkowski',
#              'rogerstanimoto','russelrao','seuclidean','sokalmichener',
#              'sokalsneath','sqeuclidean','yule']

 distancia = 'euclidean'

# Numero de amostras
 Nobj = data.shape[0]

# Total de classes
 Nclasses = max(cl.values())

# Total de amostras por classe
# assumindo que a base é balanceada!!!!
 Nac = Nobj/Nclasses

# Numero de recuperações
 Nretr = Nac

# Calcula matriz de distancias 
 md = squareform(pdist(data,distancia))

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
  classe_retrs = aux[1:Nretr]
  n = scipy.nonzero(classe_retrs == classe_padrao)
 # Contabiliza resultados
  for i in n[0]:
   l[classe_padrao-1,i] = l[classe_padrao-1,i] + 1 

 return l,Nac

# -------------------------- Programa Principal ---------------------------
#
# Dicionários de entrada (linha de comando)
# Cada dicionário é uma base de dados de vetores de características
# de um método diferente de extração de características
db = [cPickle.load(open(n)) for n in sys.argv[1:]]

# Lista para armazenar os resultados dos experimentos CBIR
res = []
# Realiza varios experimentos e gera lista com os resultados
for l in db:
 aux = Experimento(l)
 res.append(PrecisionByRecall.PrecisionByRecall(aux[0],aux[1]))

# Gráficos dos resultados
for r in res:
 pylab.plot(r.recall,r.precision)

pylab.show()

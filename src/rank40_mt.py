#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import cPickle
import scipy
# Jensen-shannon divergence
import jsd
# Hellinger distance
import hellinger as He
import Patrick_Fisher
from multiprocessing import Queue,Process
from pdist2 import pdist3

# Jensen-Shannon divergence
distancia = jsd.jsd
# Hellinger divergence
#distancia = He.He
#distancia = Patrick_Fisher.Patrick_Fisher

def worker(in_q,out_q):
    args = in_q.get()
    pid = args[0]
    X = args[1]
    idx = args[2]
    d = pdist3(X,distancia,idx)
    out_q.put([pid,d])
    return

if __name__ == '__main__':

# print "abrindo databases"
# databases
# Curvaturas
# print sys.argv[1]
 db1 = cPickle.load(open(sys.argv[1]))
# Angle sequence signature
# print sys.argv[2]
 db2 = cPickle.load(open(sys.argv[2]))
# Centroid distance
# print sys.argv[3]
 db3 = cPickle.load(open(sys.argv[3]))

# Area integral invariant
# print sys.argv[4]
 db4 = cPickle.load(open(sys.argv[4]))

# nome das figuras
 name_arr = scipy.array(db1.keys())

# dicionario nome das figuras - classes
 cl = dict(zip(name_arr,[db1[n][0] for n in name_arr]))

# print "gerando base de histogramas"
# vetores de caracteristicas e classes
#data = scipy.array([scipy.fromstring(db[nome],sep=' ')[0:70] for nome in name_arr])
 data = scipy.array([[db1[n][1:],db2[n][1:],db3[n][1:],db4[n][1:]] for n in name_arr])

# Numero de amostras
 Nobj = data.shape[0]
	
 in_q,out_q = Queue(),Queue()

 threads = []
 for i in range(8):
    t =  Process(target=worker,args=(in_q,out_q))
    threads.append(t)

 for p in threads:
  p.start()

 idx_l = scipy.arange(0,Nobj,2)
 idx_h = scipy.arange(1,Nobj+1,2) 
# print "Calculando matriz de distancias"
 in_q.put([0,scipy.vstack(data[:,0]),idx_l])
 in_q.put([1,scipy.vstack(data[:,0]),idx_h])
 in_q.put([2,scipy.vstack(data[:,1]),idx_l])
 in_q.put([3,scipy.vstack(data[:,1]),idx_h])
 in_q.put([4,scipy.vstack(data[:,2]),idx_l])
 in_q.put([5,scipy.vstack(data[:,2]),idx_h])
 in_q.put([6,scipy.vstack(data[:,3]),idx_l])
 in_q.put([7,scipy.vstack(data[:,3]),idx_h])
 
 
# pesos das caracteristicas para o cálculo da distância 
# distancia : medida de dissimilaridade a ser empregada 
#distancias = ['braycurtis','canberra','chebyshev','cityblock','correlation',
#              'cosine','dice','euclidean','hamming','jaccard',
#              'kulsinski','mahalanobis','matching','minkowski',
#              'rogerstanimoto','russelrao','seuclidean','sokalmichener',
#              'sokalsneath','sqeuclidean','yule']

# Numero de recuperacoes para o cálculo do Bull eye
 Nretr = 40

# Aqui vai dormir e acordar quando tiver o resultado
# de cada matriz de distancias 

 l = [out_q.get() for i in scipy.arange(8)]
 d1 = scipy.zeros((Nobj,Nobj))
 d2 = scipy.zeros((Nobj,Nobj))
 d3 = scipy.zeros((Nobj,Nobj))
 d4 = scipy.zeros((Nobj,Nobj))

 for a in l:
  if a[0] in [0,1]:
   d1 = d1 + a[1]
  elif a[0] in [2,3]:
   d2 = d2 + a[1]
  elif a[0] in [4,5]:
   d3 = d3 + a[1]
  else:
   d4 = d4 + a[1]
 
 w1,w2,w3,w4 = (0.25,0.25,0.25,0.25)

 md = w1*d1 + w2*d2 + w3*d3 + w4*d4

# Acumulador para contabilizar desempenho do experimento
 tt = 0

 #print "Calculando bull eye score"
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
 print tt/float(1400*20)  


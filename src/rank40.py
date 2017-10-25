#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-
import sys
import pickle
import scipy
import jsd
import hellinger as He
import Patrick_Fisher as pf
import chi_square
import dkl

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
    # Area integral invariant,fix_imports = True,encoding='iso-8859-1'

    p[i,j] = w1*d1+w2*d2+w3*d3
 p = p + p.transpose()
 return p

#print "abrindo databases"
# databases
# Curvaturas
db1 = pickle.load(open(sys.argv[1],"rb"))
# Angle sequence signature
db2 = pickle.load(open(sys.argv[2],"rb"))
# Centroid distance
db3 = pickle.load(open(sys.argv[3],"rb"))

dist = sys.argv[4]

w1 = float(sys.argv[5])

w2 = float(sys.argv[6])

w3 = float(sys.argv[7])

# nome das figuras
name_arr = scipy.array([i for i in iter(db1.keys())])
# dicionario nome das figuras - classes
cl = dict(zip(name_arr.tolist(),[db1[n][0] for n in iter(db1.keys())]))

#print "gerando base de histogramas"
# vetores de caracteristicas e classes
#data = scipy.array([scipy.fromstring(db[nome],sep=' ')[0:70] for nome in name_arr])
data = scipy.array([[db1[n][1:],db2[n][1:],db3[n][1:]] for n in name_arr])


##################################################
# TEM DE ESPECIFICAR AQUI QUAL DISTANCIA UTILIZAR
#####################################3############
dist_dict = {"HE":He.He,"JS":jsd.jsd,"PF":pf.Patrick_Fisher,"CS":chi_square.chi_square}

distancia = dist_dict[dist]

##########################################
# Numero de amostras da base
##########################################
Nobj = data.shape[0]

###################################################################
# Numero de recuperacoes (o dobro to total de amostras por classe)
###################################################################
# Total de classes
Nclasses = max(cl.values())

# Total de amostras por classe
# assumindo que a base e balanceada!!!!
Nac = int(Nobj/Nclasses)

# Numero de recuperacoes
Nretr = 2*Nac

# Acumulador para contabilizar desempenho do experimento
tt = 0

# Calcula matriz de distancias 
#print "Calculando matriz de distancias"
md = pdist(data,distancia)

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
print(tt/float(Nobj*Nac))  

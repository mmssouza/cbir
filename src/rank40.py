# -*- coding: iso-8859-1 -*-
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
def pdist(X,dist_func,w1,w2,w3):
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

def rank40(tmp0,tmp1,tmp2,args):
 db1 = pickle.load(open(tmp0,"rb"))
 # Angle sequence signature
 db2 = pickle.load(open(tmp1,"rb"))
 # Centroid distance
 db3 = pickle.load(open(tmp2,"rb"))

 w1,w2,w3 = args[0],args[1],args[2]
 # nome das figuras
 name_arr = scipy.array([i for i in iter(db1.keys())])
 # dicionario nome das figuras - classes
 cl = dict(zip(name_arr.tolist(),[db1[n][0] for n in iter(db1.keys())]))

 # vetores de caracteristicas e classes
 data = scipy.array([[db1[n][1:],db2[n][1:],db3[n][1:]] for n in name_arr])


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

###################################################################
# Numero de recuperacoes (o dobro to total de amostras por classe)
###################################################################
 Nretr = 10

# Acumulador para contabilizar desempenho do experimento
 tt = 0

# Calcula matriz de distancias 
#print "Calculando matriz de distancias"
 md = pdist(data,distancia,w1,w2,w3)

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
 return (100*tt/float(Nobj*5))  


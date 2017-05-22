# -*- coding: iso-8859-1 -*-
import pickle
import scipy
import jsd
import chi_square
import hellinger as He
import Patrick_Fisher
from multiprocessing import JoinableQueue,Queue,Process
from pdist2 import pdist3
import settings

# Jensen-Shannon divergence
dd = {"Hellinger":He.He,"Jensen Shannon":jsd.jsd,"Patrick Fisher":Patrick_Fisher.Patrick_Fisher,"Chi Square":chi_square.chi_square}
distancia = dd[settings.distancia]
# Hellinger divergence
#distancia = He.He
#distancia = Patrick_Fisher.Patrick_Fisher
#distancia = chi_square.chi_square

def worker(in_q,out_q):
 while True:   
    args = in_q.get()
    pid = args[0]
    X = args[1]
    idx = args[2]
    d = pdist3(X,distancia,idx)
    out_q.put([pid,d])
    in_q.task_done()

def rank40(tmp0,tmp1,tmp2,args):

# print "abrindo databases"
# databases
# Curvaturas
# print sys.argv[1]
 db1 = pickle.load(open(tmp0,'rb'))
# Angle sequence signature
# print sys.argv[2]
 db2 = pickle.load(open(tmp1,'rb'))
# Centroid distance
# print sys.argv[3]
 db3 = pickle.load(open(tmp2,'rb'))

# nome das figuras
 name_arr = scipy.array([k for k in iter(db1.keys())])

# dicionario nome das figuras - classes
 cl = dict(zip(name_arr,[db1[n][0] for n in name_arr]))

# print "gerando base de histogramas"
# vetores de caracteristicas e classes
#data = scipy.array([scipy.fromstring(db[nome],sep=' ')[0:70] for nome in name_arr])
 data = scipy.array([[db1[n][1:],db2[n][1:],db3[n][1:]] for n in name_arr])

# Numero de amostras
 Nobj = data.shape[0]


 in_q,out_q = JoinableQueue(),Queue()

 threads = []
 for i in range(settings.Nthreads):
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
 
# Aqui vai dormir e acordar quando tiver processado
# cada fragmento da matriz de distancias 

 in_q.join()

# Recupera os resultados

 l = []
 for i in range(6):
   l.append(out_q.get())
 
 for t in threads:
    t.terminate() 
    
# Constroi a matriz de distâncias a partir dos resultados
# parciais
 
 d1 = scipy.zeros((Nobj,Nobj))
 d2 = scipy.zeros((Nobj,Nobj))
 d3 = scipy.zeros((Nobj,Nobj))
 
 for a in l:
  if a[0] in [0,1]:
   d1 = d1 + a[1]
  elif a[0] in [2,3]:
   d2 = d2 + a[1]
  elif a[0] in [4,5]:
   d3 = d3 + a[1]
  
 w1,w2,w3 = args[0],args[1],args[2]

 md = w1*d1 + w2*d2 + w3*d3
# md = scipy.sqrt(d1) + scipy.sqrt(d2) + scipy.sqrt(d3) + scipy.sqrt(d4)
# md = d1**2 + d2**2 + d3**2 + d4**2
#md = (d1*d2*d3*d4)**0.25
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
  classe_retrs = aux[0:settings.Nretr]
  # Contabiliza desempenho contando o número de formas da mesma classe
  # do modelo (tp) dentre as 40 recuperadas
  # Atualiza o resultado acumulado (tt)
  n = scipy.nonzero(scipy.array(classe_retrs) == classe_padrao)
  tp = float(n[0].size)
  tt = tt + tp
    
# Bull eye
 return tt/float(Nobj*int(settings.Nretr/2))  


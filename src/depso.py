import scipy
import numpy as np
from numpy.random import shuffle,random_integers,rand
import scipy.spatial.distance

class de:

 def __init__(self,fitness_func,npop = 10,pr = 0.7,beta = 2.5,debug=False):
  self.ns = npop
  self.bmax = beta
  self.pr  = pr 
  self.debug = debug
  self.fitness_func = fitness_func
  self.fit = scipy.zeros((self.ns,1))
  self.pop = []
  # avalia fitness de toda populacao
  for i in scipy.arange(self.ns):
   self.fit[i],aux = self.avalia_aptidao(self.gera_individuo())
   #print i,self.fit[i]
   self.pop.append(aux.copy())
  self.pop = scipy.array(self.pop)
 
 def gera_individuo(self):
   
   l = []
   #aii
   l.append(0.1 + 0.85*rand()) # 0 raio
   l.append(5+500*rand()) # 1 bins
   l.append(0.2*rand()) # 2 hist range min
   l.append(0.7 + 0.3*rand()) # 3 hist range max
   #curv
   l.append(6+rand()*50) # 4 sigma
   l.append(5+500*rand()) # 5 bins
   a = rand(2)
   l.append(-200-6000*a.min()) # 6 hist range min
   l.append(200+6000*a.max()) # 7 hist range max
   #angle
   l.append(5+45*rand()) # 8 raio
   l.append(5+500*rand()) # 9 bins
   l.append(0.2*rand()) # 10 hist range min
   l.append(np.pi - 1.5*rand()) # 11 hist range max 
   l.append(10+rand()*40) # 12 sigma
   #cd
   l.append(5+500*rand()) # 13  bins
   l.append(0.2*rand()) # 14 hist range min
   l.append(0.7 + 0.3*rand()) # 15 hist range max
   l.append(10+rand()*40) # 16 sigma


   return np.array(l) 

 def avalia_aptidao(self,x):
  if not 0.1 <= x[0] <= 0.85: # 0 raio
   x[0] = 0.1 + 0.85*rand() 
  if not 5.0 <= x[1] <= 500.0: # 1 bins
   x[1] = 5+500*rand() 
  if not 0.0 <= x[2] <= 0.2: # 2 hist range min
   x[2] = 0.2*rand()
  if not 0.7 <= x[3] <= 1.0: # 3 hist range max
   x[3] = 0.7 + 0.3*rand()
  if not 6.0 <= x[4] <= 56.0: # 4 sigma
   x[4] = 6+rand()*50
  if not 5.0 <= x[5] <= 500.0: # 5 bins
   x[5] = 5+500*rand()
  if not -6200.0 <= x[6] <= -200.0: # 6 hist range min
   x[6] = -200-6000*rand()
  if not 200 <= x[7] <= 6200: # 7 hist range max
   x[7] = 200+6000*rand()
  if not 5. <= x[8] <= 50.: # 8 raio
   x[8] = 5+45*rand()
  if not 5.0 <= x[9] <= 500.0: # 9 bins
   x[9] = 5+500*rand()  
  if not 0.0 <= x[10] <= 0.2: # 10 hist range min
   x[10] = 0.2*rand() 
  if not 1.64 <= x[11]<= np.pi: # 11 hist range max
   x[11] = np.pi - 1.5*rand()
  if not 10.<=x[12]<=50.: # 12 sigma
   x[12] = 10+rand()*40
  if not 5.0 <= x[13] <= 500.0: # 13 bins 
   x[13] = 5+500*rand()
  if not 0.0 <= x[14] <= 0.2: # 14 hist range min
   x[14] = 0.2*rand()
  if not 0.7 <= x[15] <= 1.0: # 15 hist range max
   x[15] = 0.7 + 0.3*rand()
  if not 10.<=x[16]<=50.0:  # 16 sigma
   x[16] = 10+rand()*40

  return (self.fitness_func(x),x)
   
 def individuo_valido(self,x):  
  valido = False
  
  return valido 
  
 def run(self):
  #prox_geracao = []
   
  for i in scipy.arange(self.ns):
   if self.debug: print "i = {0}".format(i)
   # para cada individuo da populacao 
   # gera trial vector usado para perturbar individuo atual (indice i)
   # a partir de 3 individuos escolhidos aleatoriamente na populacao e
   # cujos indices sejam distintos e diferentes de i  
   invalido = True
   while invalido:
    j = random_integers(0,self.ns-1,3)
    invalido = (i in j)
    invalido = invalido or (j[0] == j[1]) 
    invalido = invalido or (j[1] == j[2]) 
    invalido = invalido or (j[2] == j[0])
    if self.debug: print "j (mutacao) = {0}".format(j)
    if self.debug: print "invalido flag = {0}".format(invalido)
   
   if self.debug: print "j (mutacao) = {0}".format(j)
 
   self.beta = self.bmax*(1.+scipy.rand())
   # trial vector a partir da mutacao de um alvo 
   u = self.pop[j[0]] + self.beta*(self.pop[j[1]] - self.pop[j[2]])
   if self.debug: print "u (target vector) = {0}".format(u)

   # gera por crossover solucao candidata
   c = self.pop[i].copy()  
   # seleciona indices para crossover
   # garantindo que ocorra crossover em
   # pelo menos uma vez
   j = random_integers(0,self.pop.shape[1]-1)
  
   for k in scipy.arange(self.pop.shape[1]):
    if (scipy.rand() < self.pr) or (k == j):
     c[k] = u[k]  

   c_fit,c = self.avalia_aptidao(c) 

   if self.debug: print "atual = {0}, fitness = {1}".format(self.pop[i],self.fit[i])
   if self.debug: print "candidato = {0}, fitness = {1}".format(c,c_fit)
    
   # leva para proxima geracao quem tiver melhor fitness
   if c_fit > self.fit[i]:
    self.pop[i] = c
    self.fit[i] = c_fit

  # avalia fitness da nova populacao
#  for i in scipy.arange(self.ns):
#   self.fit[i],self.pop[i] = self.avalia_aptidao(self.pop[i]) 
  
class pso:

 def __init__(self,fitness_func,npop = 20,w = 0.5,c1 = 2.01,c2 = 2.02,debug = False):
  self.debug = debug
  self.c1 = c1
  self.c2 = c2
  self.w = w
  self.ns = npop
  # gera pop inicial
  # centroides dos Kmax agrupamentos 
  self.pop = scipy.array([self.gera_individuo() for i in scipy.arange(self.ns)])
  self.fitness_func = fitness_func
  self.fit = scipy.zeros(self.ns)
  # avalia fitness de toda populacao
  for i in scipy.arange(self.ns):
   self.fit[i],aux = self.avalia_aptidao(self.pop[i])
   self.pop[i] = aux.copy()
  
  # inicializa velocidades iniciais
  self.v = scipy.zeros(self.pop.shape)
  # guarda a melhor posicao de cada particula 
  self.bfp = scipy.copy(self.pop)
  self.bfp_fitness = scipy.copy(self.fit)
  # guarda a melhor posicao global
  self.bfg = self.pop[self.bfp_fitness.argmax()]
 
 def gera_individuo(self):
   return x

 def avalia_aptidao(self,x): 
   fit = self.fitness_func(label_pred,self.X)
   return (fit,x)
 
 def individuo_valido(self,x):  
  valido = False
  return valido 
 
 def run(self):
  # Para cada particula 
  for i in scipy.arange(self.ns):
   # atualiza melhor posicao da particula
   self.fit[i],aux = self.avalia_aptidao(self.pop[i])
   self.pop[i] = aux.copy()
   # atualiza melhor posicao da particula
   self.bfp_fitness[i],aux = self.avalia_aptidao(self.bfp[i])
   self.bfp[i] = aux.copy()
   if self.debug:
    print "self.fit[{0}] = {1} bfp_fitness = {2}".format(i,self.fit[i],self.bfp_fitness[i])
   if self.bfp_fitness[i] < self.fit[i]:
    self.bfp[i] = self.pop[i].copy()
    self.bfp_fitness[i] = self.fit[i].copy()
  
  # Atualiza melhor posicao global
  idx = self.bfp_fitness.argmax()
  curr_best_global_fitness = self.bfp_fitness[idx]
  curr_best_global = self.bfp[idx].copy()
  if curr_best_global_fitness > self.bfp_fitness.max():
    self.bfg = curr_best_global
 
  for i in scipy.arange(self.ns):
   # Atualiza velocidade
   self.v[i] = self.w*self.v[i] 
   self.v[i] = self.v[i] + self.c1*scipy.rand()*( self.bfp[i] - self.pop[i]) 
   self.v[i] = self.v[i] + self.c2*scipy.rand()*(self.bfg - self.pop[i])
   # Atualiza posicao
   self.pop[i] = self.pop[i] + self.v[i]
   
  # calcula fitness 
   self.fit[i],aux = self.avalia_aptidao(self.pop[i])
   self.pop[i] = aux.copy()
   
    

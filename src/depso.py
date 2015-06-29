import scipy
import numpy as np
from numpy.random import shuffle,random_integers,rand
import scipy.spatial.distance

class de:

 def __init__(self,fitness_func,npop = 10,pr = 0.7,beta = 5.0,debug=False):
  self.ns = npop
  self.bmax = beta
  self.pr  = pr 
  self.debug = debug
  self.pop = [self.gera_individuo() for i in scipy.arange(self.ns)]
  self.fitness_func = fitness_func
  self.fit = scipy.zeros((self.ns,1))
  # avalia fitness de toda populacao
  for i in scipy.arange(self.ns):
   self.fit[i],aux = self.avalia_aptidao(self.pop[i])
   self.pop[i] = aux.copy()
 
 def gera_individuo(self):
   
   l = []
   #aii
   l.append(0.1 + 0.85*rand()) # raio
   l.append(5+500*rand()) # bins
   l.append(0.2*rand()) # hist range min
   l.append(1.0 - 0.3*rand()) # hist range max
   #curv
   l.append(20+rand()*20) # sigma
   l.append(5+500*rand()) # bins
   a = rand(2)
   l.append(-200-4000*a.min()) # hist range min
   l.append(200+4000*a.max()) # hist range max
   #angle
   l.append(15+5*rand()) # raio
   l.append(5+500*rand()) # bins
   l.append(rand()) # hist range min
   l.append(1.5 + (np.pi - 1.5)*rand()) # hist range max
   #cd
   l.append(5+500*rand()) # bins
   l.append(0.15*rand()) # hist range min
   l.append(0.25 + 0.75*rand()) # hist range max

   return np.array(l) 

 def avalia_aptidao(self,x):
  return (self.fitness_func(x),x)
   
 def individuo_valido(self,x):  
  valido = False
  
  return valido 
  
 def run(self):
  prox_geracao = []
   
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
   # seleciona indices para crossover
   # garantindo que ocorra crossover em
   # pelo menos uma vez
   j = [random_integers(0,1)]
   for k in scipy.arange(2):
    if (scipy.rand() < self.pr) and (k != j[0]):
     j.append(k)

   if self.debug: print "j (crossover) = {0}".format(j)

   # gera por crossover solucao candidata
   c = self.pop[i].copy()
   for k in j:
    c[k] = u[k]
   
   c_fit,c = self.avalia_aptidao(c) 

   if self.debug: print "atual = {0}, fitness = {1}".format(self.pop[i],self.fit[i])
   if self.debug: print "candidato = {0}, fitness = {1}".format(c,c_fit)
    
   # leva para proxima geracao quem tiver melhor fitness
   if c_fit > self.fit[i]:
    prox_geracao.append(c)
   else:
    prox_geracao.append(self.pop[i])           
 
  self.pop = scipy.array(prox_geracao)
  # avalia fitness da nova populacao
  for i in scipy.arange(self.ns):
   self.fit[i],self.pop[i] = self.avalia_aptidao(self.pop[i]) 
  
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
   
    

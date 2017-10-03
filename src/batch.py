#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import subprocess
import tempfile
import os
import csv
import sys
import pickle

diretorio = sys.argv[1] # Diretorio das bases de imagens

cl = pickle.load(open(diretorio+"classes.txt","rb")) # dicionario nomes das formas - classes
fnames = pickle.load(open(diretorio+"names.pkl","rb")) # nomes da formas de interesse

csv_data = [i for i in csv.reader(open("resultados.csv","r"))] # Le conteúdo do arquivo csv

dist_list = [i[1] for i in csv_data[2:]] # Despreza as duas primeiras linhas e obtêm apenas os nomes das distâncias usadas em cada otimização

params_dict = {"JS":[],"HE":[],"PF":[],"CS":[]}

for i,p in enumerate([l[2:] for l in csv_data[2:]]):
 d = dist_list[i]
 params_dict[d].append(p)   

for dist,params_list in params_dict.items():
 for param in params_list:
  bull_eye_opt = param[0]   
  curv_args = param[1:5]
  angle_args = param[5:8]
  cd_args = param[8:10]
  rank_args = param[10:13] 
  
  print(dist,curv_args,angle_args,cd_args,rank_args)
  
  tmp0 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
  tmp1 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
  tmp2 = tempfile.NamedTemporaryFile(suffix ='.pkl',dir='/tmp',delete = False)
 
  print("passo 1 - Extracao caracteristicas")
  p_curv = subprocess.Popen(['./gera_curvatura_sig.py',diretorio]+curv_args+[tmp0.name])
  p_angle = subprocess.Popen(['./gera_angle_sig.py',diretorio]+angle_args+[tmp1.name])
  p_cd = subprocess.Popen(['./gera_cd_sig.py',diretorio]+cd_args+[tmp2.name])

  p_cd.wait()
  p_angle.wait()
  p_curv.wait()
  
  print("passo 2 - Experimento Shape retrieval")
  cmd = " ".join(['./rank.py',tmp0.name,tmp1.name,tmp2.name,dist]+rank_args)
  res = subprocess.getoutput(cmd)
  
  print(bull_eye_opt,res)

  os.remove(tmp0.name)
  os.remove(tmp1.name)
  os.remove(tmp2.name)

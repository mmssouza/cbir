#!/bin/bash

curv_fname="curvatura_sig.pkl"
cd_fname="cd_sig.pkl"
angle_fname="angle_sig.pkl"

echo $curv_fname
echo $cd_fname
echo $angle_fname

./gera_curvatura_sig.py $1 20. 155 -16000 16000 $curv_fname
./gera_cd_sig.py $1 10 0 1. 75 $cd_fname
./gera_angle_sig.py $1 5 10 0 1. 75 $angle_fname

./rank40.py $curv_fname $cd_fname $angle_fname
./rank.py  $curv_fname $cd_fname $angle_fname 

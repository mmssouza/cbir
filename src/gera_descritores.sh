#!/bin/bash

curv_fname="curvatura_sig.pkl"
cd_fname="cd_sig.pkl"
angle_fname="angle_sig.pkl"

echo $curv_fname
echo $cd_fname
echo $angle_fname

./gera_curvatura_sig.py $1 85. 204 -13939 7799 $curv_fname
./gera_cd_sig.py $1 84 0 1. 89.4 $cd_fname
./gera_angle_sig.py $1 0.351 123 77.7 $angle_fname

./rank40.py $curv_fname $cd_fname $angle_fname 0.29 0.724 0.965
./rank.py  $curv_fname $cd_fname $angle_fname 0.29 0.724 0.965

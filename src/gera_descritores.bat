
@set curv_fname="curvatura_sig.pkl"
@set cd_fname="cd_sig.pkl"
@set angle_fname="angle_sig.pkl"
python gera_curvatura_sig.py %1 20 155 -16000 16000 %curv_fname%
python gera_cd_sig.py %1 10 100 %cd_fname%
python gera_angle_sig.py %1 0.351 123 77.7 %angle_fname%

rank40.py %curv_fname% %cd_fname% %angle_fname% HE 0.29 0.724 0.965
rank.py  %curv_fname% %cd_fname% %angle_fname% HE 0.29 0.724 0.965
